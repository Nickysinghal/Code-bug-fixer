from flask import Flask, redirect, request, render_template
import openai
from openai import OpenAI
import os
from dotenv import load_dotenv #as flask itself doesn’t automatically read .env
load_dotenv() #load .env file
import hashlib
import sqlite3
import stripe

app = Flask(__name__)

#loads api key from .env
OPENROUTER_API_KEY= os.getenv("openrouter_api_key")
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")


#function to create a database
def initialize_database():
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (fingerprint text primary key, usage_counter integer)''')
    # migrate: add usage_counter if missing
    c.execute("PRAGMA table_info(users)")
    cols = [row[1] for row in c.fetchall()]
    if 'usage_counter' not in cols:
        c.execute("ALTER TABLE users ADD COLUMN usage_counter INTEGER DEFAULT 0")
    
    conn.commit()
    conn.close()

#to get browsers fingerprint(unique key)
def get_fingerprint():
    browser = request.user_agent.browser
    version = request.user_agent.version and float(request.user_agent.version.split(".")[0])
    platform = request.user_agent.platform
    string = f"{browser}:{version}:{platform}"
    fingerprint = hashlib.sha256(string.encode("utf-8")).hexdigest()
    print(fingerprint)
    return fingerprint

#to get usage counter (how many times the user has used service) for a particular fingerprint and if fingerprint does not exist we will add it with counter 0
def get_usage_counter(fingerprint):
    conn = sqlite3.connect('app.db')
    c= conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (fingerprint text primary key, usage_counter int)''')
    
    result = c.execute('SELECT usage_counter FROM users WHERE fingerprint=?',[fingerprint]).fetchone()
    if result is None:
        conn = sqlite3.connect('app.db')
        c= conn.cursor()
        c.execute('INSERT INTO users (fingerprint, usage_counter) VALUES(?,0)',[fingerprint])
        conn.commit()
        conn.close()
        return 0
    
    r =result[0]
    print("thee RREESSUULLTT r is",result)
    conn.close()
    return r
    
#function to update the usage counter
def update_usage_counter(fingerprint,usage_counter):
    conn = sqlite3.connect('app.db')
    c=conn.cursor()
    c.execute('UPDATE users SET usage_counter=? WHERE fingerprint=?',
              [int(usage_counter)+1,fingerprint])
    conn.commit()
    conn.close()
        

#Api token
# openai.api_key="YOUR_API_KEY"  or
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key= OPENROUTER_API_KEY,
)

@app.route("/",methods=["GET","POST"])
def index():
    initialize_database()
    fingerprint = get_fingerprint()
    usage_counter = get_usage_counter(fingerprint)
    
    
    if request.method=="POST":
        if usage_counter>1: #you can run only 2 times
            return render_template("payment.html")
        # Code Err
        code = request.form["code"]
        error = request.form["error"]
        
        prompt = (f"Explain the error in this code without fixing it:"
                  f"\n\n{code}\n\nError:{error}")
        model_engine = "openai/gpt-4o"
        
        explaination_completions = client.chat.completions.create(
            model=model_engine,
            messages=[
                {
                "role": "user",
                "content": prompt,
                }
            ],
            n=1,
            temperature=0.9,
            max_tokens= 1024,
        )
        
        explaination = explaination_completions.choices[0].message.content
        
        fixed_code_prompt = (f"Fix this code: \n \n {code}\n\nError:\n\n{error}"
                  f"\n Respond only with the fixed code")
        fixd_code_completions = client.chat.completions.create(
            model=model_engine,
            messages=[
                {
                "role": "user",
                "content": fixed_code_prompt,
                }
            ],
            n=1,
            temperature=0.9,
            max_tokens= 1024,
        )
        
        fixed_code = fixd_code_completions.choices[0].message.content
        #calling function to update usage counter
        update_usage_counter(fingerprint,usage_counter)
        
        return render_template("index.html",explaination=explaination,fixed_code=fixed_code)
    
    return render_template("index.html")

@app.route("/create-checkout-session", methods=["POST"])
def create_checkout_session():
    amount = int(request.form["amount_key"])
    plan = request.form["plan_key"]

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        mode="payment",
        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": {"name": plan},
                "unit_amount": amount,
            },
            "quantity": 1,
        }],
        success_url="http://localhost:5000/success?amount={}&plan={}".format(amount, plan),
        cancel_url="http://localhost:5000/cancel",
    )
    return redirect(session.url, code=303)
 #show congrates u have purchased successfull along with amount
 
 
@app.route("/success")
def success():
    return "<h1> Payment successful!</h1>"

@app.route("/cancel")
def cancel():
    return "<h1> Payment cancelled.</h1>"




if __name__=="__main__":
    app.run(debug=True)
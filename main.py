from flask import Flask, request, render_template
import openai
from openai import OpenAI
import os
from dotenv import load_dotenv #as flask itself doesn’t automatically read .env
load_dotenv() #load .env file

app = Flask(__name__)

#loads api key from .env
OPENROUTER_API_KEY= os.getenv("openrouter_api_key")

#Api token
# openai.api_key="YOUR_API_KEY"  or
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key= OPENROUTER_API_KEY,
)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
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
        
        return render_template("index.html",explaination=explaination,fixed_code=fixed_code)
    
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)
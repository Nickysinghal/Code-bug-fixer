# 🐞 Code Bug Fixer

A simple AI-powered web app built using **Flask** and **OpenAI (via OpenRouter API)** that helps you:
- Fix buggy code automatically  
- Explain the reason behind the error
- Manage limited free trials and upgrade for continued access

---

## 🚀 Features
- 🧠 Uses GPT-based models from OpenRouter (e.g. `gpt-4o-mini`)
- 💡 Explains code errors in plain English
- 🔧 Automatically generates corrected code
- 💰 2 free trial fixes for new users, then requires payment
- 💳 Stripe integration for secure checkout and subscription handling
- 🌐 Clean, responsive web interface built with HTML + CSS

---

## 📁 Project Structure
```
code-bug-fixer/
│
├── static/
│   └── style.css             # App styling (HTML/CSS)
│
├── templates/                # Flask HTML templates
│   ├── index.html            # Main homepage (code input + results)
│   ├── charge.html           # Stripe payment processing page
│   └── payment.html          # Payment/checkout UI
│
├── app.py                    # Main Flask application (routes + logic)
├── app.db                    # SQLite database (user/trial tracking)
├── .env                      # API keys and configuration
├── .gitignore                # Ignored files for Git
├── requirements.txt          # Python dependencies
└── README.md                 # Documentation

```
---

## ⚙️ Installation & Setup

### 1️⃣ Clone this repository
```bash
git clone https://github.com/Nickysinghal/code-bug-fixer.git
cd code-bug-fixer
```
### 2️⃣ Create a virtual environment
For Windows:
```
python -m venv venv
venv\Scripts\activate
```
For macOS / Linux:
```
python3 -m venv venv
source venv/bin/activate
```
### 3️⃣ Install required packages
```
pip install -r requirements.txt
```
### 4️⃣ Create a file named `.env` in the project root
- Add your OpenRouter API key(You can get one from (https://openrouter.ai)):
```
OPENROUTER_API_KEY=sk-or-v1-your_api_key_here
```
- Store your secret and publishable keys safely (get it from (https://dashboard.stripe.com/test/apikeys)):
```
STRIPE_SECRET_KEY=sk_test_************************
STRIPE_PUBLISHABLE_KEY=pk_test_************************
```

🛡️ Note: Never share or commit your API key publicly!


### 5️⃣ Run the Flask app
```
python app.py
```
### 6️⃣ Open in your browser
Go to:
```
http://127.0.0.1:5000/
```
You’ll see the Code Bug Fixer interface — enter your buggy code and error message to see explanations and corrected code side-by-side.

---
## 💳 Billing / Payments

- Each user gets 2 free bug fixes on signup.
- After the free quota is used, users are redirected to the Stripe checkout page.
- Payment is processed securely using Stripe (test or live mode).
- On successful payment, users regain full access to the AI bug-fixing tool.

---
## 🧠 Logic Overview
- index.html → Main interface for entering buggy code
- Free Trial System:
  - Tracks user’s free attempts in app.db
  - Allows 2 free fixes using OpenAI/OpenRouter API
- payment.html → Triggered after trial limit is reached
- charge.html → Handles Stripe payment and success confirmation
- After successful payment, full access is restored

---
## 🧩 Example Workflow
Paste your Python (or JS/C/Java) code in the “Enter Code” box

Paste the compiler/interpreter error in the “Enter Error” box

Click “Fix Code”

The right panel will display:

✅ Fixed code

💬 Explanation of what went wrong

---

## 💳 Stripe Test Payment Details

Use these cards in **Test Mode** (no real money charged):

- ✅ **Success:** `4242 4242 4242 4242`
- ❌ **Declined:** `4000 0000 0000 0002`
- ⚠️ **Insufficient Funds:** `4000 0000 0000 9995`
- 🔐 **3D Secure (Success):** `4000 0025 0000 3155`
- 🔐 **3D Secure (Fail):** `4000 0000 0000 3063`

**Other fields:**
- Expiry: any future date (e.g. `12 / 34`)  
- CVC: any 3 digits (e.g. `123`)  
- ZIP: any 5 digits (e.g. `12345`)  


---

## 🧱 Technologies Used
- Backend: Flask (Python)

- Frontend: HTML, CSS

- AI Engine: OpenRouter API (GPT-4o-mini)
- Payments: Stripe

- Environment Management: python-dotenv, venv

---

### ⚠️ Important Notes
- Keep .env in .gitignore to protect your API key.

- If deploying on Render/Railway, add OPENROUTER_API_KEY in their Environment Variables section.

- Compatible with Python 3.8+

---

## 🧑‍💻 Author
Nicky Singhal
📧 nickysinghal111@gmail.com
🌐 [GitHub Profile](https://github.com/Nickysinghal)

--- 

### 🟢 License
This project is open-source under the MIT License.


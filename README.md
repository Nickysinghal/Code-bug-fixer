# 🐞 Code Bug Fixer

A simple AI-powered web app built using **Flask** and **OpenAI (via OpenRouter API)** that helps you:
- Fix buggy code automatically  
- Explain the reason behind the error  

---

## 🚀 Features
- 🧠 Uses GPT-based models from OpenRouter (e.g. `gpt-4o-mini`)
- 💡 Explains code errors in plain English
- 🔧 Automatically generates corrected code
- 🌐 Clean, responsive web interface built with HTML + CSS

---

## 📁 Project Structure
```
code-bug-fixer/
│
├── app.py # Flask application
├── templates/
│ └── index.html # HTML frontend
├── static/
│ └── style.css # Styling for the app
├── requirements.txt # Python dependencies
└── .env # Environment file (store your API key here)

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
### 4️⃣ Add your OpenRouter API key
Create a file named `.env` in the project root and add:
```
OPENROUTER_API_KEY=sk-or-v1-your_api_key_here
```
🛡️ Note: Never share or commit your API key publicly!
You can get one from https://openrouter.ai

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

## 🧩 Example Workflow
Paste your Python (or JS/C/Java) code in the “Enter Code” box

Paste the compiler/interpreter error in the “Enter Error” box

Click “Fix Code”

The right panel will display:

✅ Fixed code

💬 Explanation of what went wrong

---

## 🧱 Technologies Used
- Backend: Flask (Python)

- Frontend: HTML, CSS

- AI Engine: OpenRouter API (GPT-4o-mini)

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

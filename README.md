
# 🧠 AI Agent Workflow with CrewAI + Gemini

This project is an **AI content generation pipeline** using CrewAI, LangChain, and Google Gemini (`gemini-1.5-pro`). It automates multi-step content creation through collaborative agents: **Researcher → Writer → Evaluator**.

### 🚀 Live App
👉 [Click here to open the deployed Streamlit app](https://ai-agent-workflow.streamlit.app)

---

## 💡 Features

- 🧑‍💻 Built using [CrewAI](https://github.com/joaomdmoura/crewai)
- 🔗 Powered by [LangChain](https://www.langchain.com/)
- 🤖 Uses `gemini-1.5-pro` via Google AI Studio
- 🔄 Agents collaborate using context + memory
- 🌐 Deployed on [Streamlit Cloud](https://streamlit.io/cloud)

---

## 📁 Project Structure

```bash
.
├── .env                  # API Key stored here
├── .gitignore            # Ignores venv, .env, __pycache__, etc.
├── app.py                # Streamlit frontend
├── ai_workflow.py        # Core CrewAI logic
├── requirements.txt      # All dependencies
├── .streamlit/           # Optional Streamlit config
└── README.md             # This file
```

---

## 🔐 Environment Variables

Create a `.env` file in your root directory:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

> Get your Gemini API key from: https://aistudio.google.com/app/apikey

---

## 🧪 Running Locally

```bash
git clone https://github.com/mlexpnew/ai-agent-workflow.git
cd ai-agent-workflow

# (Optional) Create virtual environment
python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## ☁️ Deployment (Streamlit Cloud)

1. Push code to GitHub
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **"New App"**
4. Connect your repo and set:
   - Branch: `main`
   - File path: `app.py`
5. Add your `GOOGLE_API_KEY` under **Secrets**

---

## 📸 UI Preview

Coming soon... (Optional: Add a screenshot or Loom video here)

---

## 🤖 Agents Overview

| Agent       | Role                      | Purpose                                 |
|-------------|---------------------------|-----------------------------------------|
| Researcher  | Research Analyst          | Gathers current and accurate insights   |
| Writer      | Content Specialist        | Drafts content from research            |
| Evaluator   | Quality Analyst           | Reviews tone, clarity, and facts        |

---

## 📦 Dependencies (`requirements.txt`)

```txt
streamlit
python-dotenv
crewai==0.22.5
langchain==0.1.20
langchain-core==0.1.53
langchain-google-genai==0.0.8
google-generativeai==0.3.2
```

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

---

> Made with ❤️ by [Your Name or Handle]


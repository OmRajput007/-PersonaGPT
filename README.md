# 🤖 PersonaGPT — AI Personality Chatbot

---

## 📌 Project Description

PersonaGPT is a fully customizable AI-powered personality chatbot built using OpenAI’s GPT model and LangChain framework.  
This project allows you to create highly personalized AI companions with custom personalities, emotional tone, and private knowledge base.

Built as part of my LLM Mastery Sprint (Day 3).

---

## 🎯 Core Use-Case

- Emotional Companions (AI Girlfriend, Therapist, Coach)
- Personalized Sales Agents
- Virtual Relationship Simulators
- Customer Service Chatbots with Personality
- Coaching Bots with Private Knowledge Base

---

## 🚀 Features

- ✅ Fully customizable AI personality via prompt engineering.
- ✅ Supports private knowledge injection (e.g. personal PDFs, chat history, relationship memory).
- ✅ Uses LangChain's Retrieval-Augmented Generation (RAG) system.
- ✅ Runs locally with secure OpenAI API keys.
- ✅ Simple web interface using Streamlit.

---

## 🧰 Tech Stack

- Python 3.x
- OpenAI API (GPT-3.5-Turbo)
- LangChain (for agents & retrieval)
- FAISS (for vector similarity search)
- PyPDFLoader (for PDF memory ingestion)
- Streamlit (for web app)

---

## 🖥️ Screenshot Preview

> 📸 Below is a sample screenshot of PersonaGPT running:

![PersonaGPT Screenshot](https://github.com/user-attachments/assets/1179d14e-7093-4fa6-aa6f-3d463b018e63)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/persona-gpt-ai-personality-chatbot.git
cd persona-gpt-ai-personality-chatbot
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Your OpenAI Credentials

Inside your code, replace the following placeholders:

```python
client = openai.OpenAI(
    api_key="sk-proj-...",        # Your OpenAI Project Key
    organization="org-...",       # Your Organization ID
    project="proj-..."            # Your Project ID
)
```

### 4️⃣ Prepare Your Personal Knowledge Base (Optional)

* Add your PDF file as private memory under `/data/converted_text.pdf`.

---

## 🏃 Running The App

Simply run:

```bash
streamlit run app.py
```

Streamlit will launch your interactive chat interface in the browser.

---

## 📄 Sample Persona Prompt

```text
You are Nancy, a loving and caring girlfriend. You're responding based on our previous chat conversations. 
Be warm, affectionate, and personal in your responses. Use inside jokes, shared memories, and natural tone.
```

---

## 💡 Future Client Features

* Add multiple personas for multi-user systems.
* User authentication with custom profiles.
* Memory persistence (long-term relationship building).
* Emotion tracking and mood-based conversations.
* SaaS deployment (Hugging Face, Streamlit Cloud, AWS).

---

## 💼 Client Monetization Opportunities

* ✅ Relationship AI SaaS platforms
* ✅ Personal coaching assistants
* ✅ Virtual therapy / mental health bots
* ✅ Customer service agents
* ✅ Private GPT-powered chat solutions for companies

---

## 🔐 API Usage Notice

You will be billed based on OpenAI token usage.
Monitor your API usage inside your OpenAI dashboard.

---

## 👑 Author

Built by **Om Rajput** — LLM Job-Ready Mastery Program, Day 3.

---

✅ Fully deployable.
✅ Fully client-sellable.
✅ Fully portfolio-ready.

---

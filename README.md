# 🤖 Gemma AI Playground
### A Local AI Chatbot Built with LangChain, Ollama, Streamlit & LangSmith

An interactive AI chatbot powered by Google's **Gemma 2B** model, running locally through Ollama and presented using Streamlit.

This project demonstrates how to build an LLM-powered application using **LangChain**, integrate locally hosted language models, manage conversational context, and monitor LLM executions using **LangSmith**.

The objective is to understand the fundamentals of Generative AI application development and LLM observability through hands-on implementation.

---

## 🚀 Features

- 💬 Interactive chatbot interface using Streamlit
- 🧠 Local LLM inference using Ollama and Gemma 2B
- 🔗 LangChain integration for LLM orchestration
- 🗂️ Conversation history and contextual prompts
- ⚙️ LangChain Expression Language (LCEL) pipeline
- 📊 LangSmith tracing and execution monitoring
- 🏷️ Execution metadata and tags
- 🔒 Local model inference without depending on a hosted LLM API

## 🏗️ Architecture

```text
             User
               |
               v
       Streamlit Interface
               |
               v
       ChatPromptTemplate
               |
               v
        LangChain Pipeline
               |
               v
        Ollama - Gemma 2B
               |
               v
         StrOutputParser
               |
               v
          AI Response

        LangSmith Monitoring
               |
               v
       Execution Traces
```

LangSmith monitors supported LangChain executions, providing visibility into prompts, model outputs, execution time, errors, and run metadata.

## 🔍 Live LangSmith Trace

Explore an actual execution trace from this project:

### [View Gemma Chatbot Execution on LangSmith](https://smith.langchain.com/o/c876dd98-ca24-4536-9ee7-6778104dbb2e/a/langchain-basics/projects/p/5b5a06ee-4ac8-496a-bb48-9d29b29db140/trace/01a20363-639f-722b-953e-77d9d76dda9e/run/01a20363-639f-722b-953e-77d9d76dda9e?scroll_to=output)

The trace demonstrates how LangSmith captures and displays an LLM execution.

**Note:** This is a workspace-specific LangSmith URL. Access may require signing in with an account that has permission to view the workspace. For unrestricted portfolio access, use a public trace-sharing link instead.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive chatbot interface |
| LangChain | LLM orchestration |
| Ollama | Local model runtime |
| Gemma 2B | Large language model |
| LangSmith | LLM tracing and observability |
| python-dotenv | Environment variable management |

## 📁 Project Structure

```text
langchain-gemma-chatbot/
│
├── .streamlit/
│   └── config.toml
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/AngadiAbhinay01/langchain-gemma-chatbot.git
```

```bash
cd langchain-gemma-chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Ollama

Download and install Ollama:

https://ollama.com/

### 4. Download the Gemma 2B model

```bash
ollama pull gemma:2b
```

Make sure Ollama is running before launching the application.

### 5. Configure LangSmith

Create a LangSmith account:

https://smith.langchain.com/

Generate a LangSmith API key.

Create a `.env` file in the project root using `.env.example` as a template.

Configure the following environment variables:

```env
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=LangChain-Gemma-Chatbot
```

**Security:** Never upload your actual `.env` file or API key to GitHub. Keep your credentials protected using `.gitignore`.

### 6. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to interact with the chatbot.

## 📊 LangSmith Monitoring

LangSmith is integrated to provide observability into the application's LLM executions.

Key monitoring capabilities:

- Prompt inputs and model outputs
- Chain execution details
- Execution latency
- Errors and debugging information
- Run metadata and tags

### Sharing LangSmith Traces

There are two ways to share project executions:

**1. Individual trace sharing**

Generate a public share link for a selected trace and share it with others. Anyone with the link may be able to inspect the shared execution.

**2. Workspace collaboration**

Invite collaborators to your LangSmith workspace, subject to available workspace permissions and plan restrictions.

Always review trace contents before sharing because prompts, inputs, outputs, and metadata may contain sensitive information.

## 📚 Key Learning Objectives

Through this project, I explored:

- Building LLM applications using LangChain
- Integrating locally hosted language models
- Working with Ollama and Gemma
- Creating and managing prompt templates
- Building LLM pipelines using LCEL
- Managing conversational context
- Integrating LangSmith for observability
- Monitoring and debugging LLM executions

## 🔮 Future Improvements

- Support for multiple local language models
- Streaming AI responses
- Improved conversation management
- Configurable model parameters
- Retrieval-Augmented Generation (RAG) integration
- Document-based question answering

## 👨‍💻 Author

**Abhinay Angadi**

Software R&D Engineer | Aspiring AI/ML Engineer

Interested in Generative AI, Large Language Models, RAG, Agentic AI, and Machine Learning.

- **GitHub:** [AngadiAbhinay01](https://github.com/AngadiAbhinay01)
- **LinkedIn:** [Abhinay Angadi](https://www.linkedin.com/in/abhinay-angadi-541004159/)

---

⭐ If you find this project useful, feel free to explore the repository and share your feedback.

**Built as part of my hands-on learning journey in Generative AI and Agentic AI.**

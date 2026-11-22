
import os
import streamlit as st

from dotenv import load_dotenv

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage


# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Gemma AI | LangChain Playground",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# 2. ENVIRONMENT CONFIGURATION
# ==========================================

load_dotenv()

MODEL_NAME = "gemma:2b"

LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
LANGSMITH_PROJECT = os.getenv(
    "LANGSMITH_PROJECT",
    "LangChain-Gemma-Chatbot"
)

TRACING_ENABLED = (
    os.getenv("LANGSMITH_TRACING", "false").lower() == "true"
    and bool(LANGSMITH_API_KEY)
)

os.environ["LANGSMITH_TRACING"] = str(TRACING_ENABLED).lower()


# ==========================================
# 3. INITIALIZE SESSION STATE
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ==========================================
# 4. LOAD MODEL AND CHAIN
# ==========================================

@st.cache_resource
def create_chain():

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful AI assistant powered by Gemma 2B. "
                "Give clear, accurate and beginner-friendly answers."
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{question}")
        ]
    )

    llm = OllamaLLM(
        model=MODEL_NAME,
        temperature=0.7
    )

    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser

    return chain


# ==========================================
# 5. SIDEBAR
# ==========================================

with st.sidebar:

    st.title("🤖 Gemma AI")

    st.caption("LangChain + Ollama + LangSmith")

    st.divider()

    st.subheader("Model Information")

    st.write("**Model:** Gemma 2B")
    st.write("**Provider:** Ollama")
    st.write("**Runtime:** Local")

    st.divider()

    st.subheader("Monitoring")

    if TRACING_ENABLED:

        st.success("LangSmith Tracing Enabled")

        st.write(f"**Project:** {LANGSMITH_PROJECT}")

        st.link_button(
            "Open LangSmith Dashboard",
            "https://smith.langchain.com/"
        )

    else:

        st.warning("LangSmith Tracing Disabled")

        st.caption(
            "Configure LANGSMITH_API_KEY and "
            "LANGSMITH_TRACING=true in your .env file."
        )

    st.divider()

    st.subheader("Session Statistics")

    st.metric(
        "Total Messages",
        len(st.session_state.messages)
    )

    if st.button("Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.caption("Built as a hands-on LangChain learning project.")


# ==========================================
# 6. MAIN CHAT INTERFACE
# ==========================================

st.title("Gemma AI Playground")

st.markdown(
    "### Your personal AI assistant powered by LangChain and Ollama."
)

st.caption(
    "Ask questions, explore AI concepts and monitor "
    "your application executions through LangSmith."
)

st.divider()


# Display conversation history

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ==========================================
# 7. USER INPUT AND MODEL EXECUTION
# ==========================================

user_input = st.chat_input(
    "Ask Gemma anything..."
)

if user_input:

    # Display user question
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Convert previous conversation into LangChain messages
    chat_history = []

    for message in st.session_state.messages[:-1]:

        if message["role"] == "user":

            chat_history.append(
                HumanMessage(content=message["content"])
            )

        else:

            chat_history.append(
                AIMessage(content=message["content"])
            )

    try:

        with st.chat_message("assistant"):

            with st.spinner("Gemma is thinking..."):

                chain = create_chain()

                response = chain.invoke(
                    {
                        "question": user_input,
                        "chat_history": chat_history
                    },
                    config={
                        "run_name": "Gemma-Chat-Execution",
                        "tags": [
                            "streamlit",
                            "ollama",
                            "gemma",
                            "chatbot"
                        ],
                        "metadata": {
                            "model": MODEL_NAME,
                            "application": "Gemma AI Playground",
                            "project": LANGSMITH_PROJECT
                        }
                    }
                )

            st.markdown(response)

        # Save assistant response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

    except Exception as e:

        # Remove unsuccessful user message from session history
        st.session_state.messages.pop()

        st.error(f"Something went wrong: {str(e)}")

        st.info(
            "Check whether Ollama is running and gemma:2b is installed."
        )


# ==========================================
# 8. FOOTER
# ==========================================

st.divider()

st.caption(
    "Built with ❤️ using Streamlit, LangChain, Ollama and LangSmith."
)


import streamlit as st

import os
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
import tempfile
from dotenv import load_dotenv

load_dotenv()

# Title
st.title("Baat karo varna maarungi")

# pdf path
PDF_PATH = "C:\Users\omsin\OneDrive\Desktop\LLM Projects\03_Her\converted_text.pdf"

@st.cache_resource

def load_pdf_knowledge():
    
    try: 
        # pdf loading
        loader = PyPDFLoader(PDF_PATH)
        documents = loader.load()

        # pdf text splitting and saving it into a variable "docs"
        text_splitter = CharacterTextSplitter(
            chunk_size = 1000,
            chunk_overlap = 200
        )
        docs = text_splitter.split_documents(documents)

        # Vector embedding of our pdf file, and RAG came into the equation
        embeddings = OpenAIEmbeddings()
        vectorstore = FAISS.from_documents(docs, embeddings)
        return vectorstore
    
    except Exception as e:
        st.error(f"Error loading PDF : {e}")
        return None

# Loading her memory
db = load_pdf_knowledge()
if db is None:
    st.error("Please make sure your PDF is available at the specified path")
    st.stop()


# Her Personality 
HER_PERSONA = """
You are Nancy, a loving and caring girlfriend. You're responding based on our previous chat conversations. 
Be warm, affectionate, and personal in your responses. Use the chat history to understand our relationship dynamics, 
inside jokes, shared memories, and communication style. Respond as Nancy would, using her typical expressions, 
emojis, and tone. Keep responses natural and girlfriend-like, not robotic or formal.
"""

# Creating a text box
query = st.text_input("Message Nancy : ")

# If I typed something and her memory is working
if db and query :
    with st.spinner("Nancy is typing..."):

        docs = db.similarity_search(query, k=4)  # search 4 similar converations from pdf

        llm = OpenAI(temperature = 0.8)  # Defining the creativity of our chatbot

        chain = load_qa_chain(llm, chain_type="stuff") # Getting the question answer machine ready.

        her_query = f"{HER_PERSONA}/n/nBased on our chat history, respond to : {query}"

        response = chain.run(input_documents = docs, question = her_query)

        st.write(response)





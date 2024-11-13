import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline

st.header("LangChain Hugging Face ChatBot")

with st.sidebar:
    st.title("Upload Document")
    file = st.file_uploader("Upload your file here", type="pdf")

if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    # Split the text into manageable chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    # Generate embeddings using SentenceTransformer
    embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = [embedding_model.encode(chunk) for chunk in chunks]

    user_question = st.text_input("Type your question here")
    if user_question:
        # Generate embedding for the user question
        question_embedding = embedding_model.encode(user_question).reshape(1, -1)

        # Compute cosine similarities between the question and each chunk
        similarities = cosine_similarity(question_embedding, embeddings).flatten()

        # Find the chunk with the highest similarity score
        best_match_idx = similarities.argmax()
        best_match_text = chunks[best_match_idx]

        # Use Hugging Face QA model
        qa_model = pipeline("question-answering", model="deepset/roberta-base-squad2")
        result = qa_model(question=user_question, context=best_match_text)

        # Display answer
        st.write("Answer:", result['answer'])
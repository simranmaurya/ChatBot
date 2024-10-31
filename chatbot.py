import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOpenAI


OPENAI_API_KEY = "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"
st.header("My ChatBot")

with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload your file here", type="pdf")


# extract text from pdf
if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text+= page.extract_text()
        #st.write(text)

    # convert text into chunks
    text_splitter = RecursiveCharacterTextSplitter(separators = "\n", 
                                                    chunk_size=1000, 
                                                    chunk_overlap = 150, 
                                                    length_function=len)
    chunks = text_splitter.split_text(text)
        # st.write(chunks)
        # print(len(chunks))

    # Generate embeddings from chunks
    embeddings = OpenAIEmbeddings(openai_api_key = OPENAI_API_KEY)

    # Vector Store
    vector_store = FAISS.from_texts(chunks,embeddings)

    # User question 
    user_question = st.text_input("Type your question here")
    if user_question:
        match = vector_store.similarity_search(user_question)

        llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature = 0.4,max_tokens = 1000, model_name = "gpt-3.5-turbo")

        chain = load_qa_chain(llm,chain_type="stuff")
        bot_response = chain.run(input_documents=match, question = user_question)
        st.write(bot_response)











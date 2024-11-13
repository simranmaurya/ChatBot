import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOpenAI


<<<<<<< HEAD
key = "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"
=======
key = "my-key"
>>>>>>> 3895d3225f6e03a206daabb786688af23d28bd43
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
    embeddings = OpenAIEmbeddings(openai_api_key=key)

    # Vector Store
    vector_store = FAISS.from_texts(chunks,embeddings)

    # User question 
    user_question = st.text_input("Type your question here")
    if user_question:
        match = vector_store.similarity_search(user_question)

<<<<<<< HEAD
        llm = ChatOpenAI(openai_api_key=key, temperature = 0.4,max_tokens = 256, model_name = "gpt-3.5-turbo")
=======
        llm = ChatOpenAI(openai_api_key=key, temperature = 0.4,max_tokens = 1000, model_name = "gpt-3.5-turbo")
>>>>>>> 3895d3225f6e03a206daabb786688af23d28bd43

        chain = load_qa_chain(llm,chain_type="stuff")
        bot_response = chain.run(input_documents=match, question = user_question)
        st.write(bot_response)











# CHATBOT

## 1. About

A simple chatbot that enables user to upload a pdf file for context and ask questions

## 2. Features

- Sidebar to upload PDF file
- Input Text Box for user questions
- Answers based on file context

## 3. Cloning the repository

- Clone the repository

```bash
(base) :~$ git clone https://github.com/simranmaurya/ChatBot.git
(base) :~$ cd CHATBOT/
(base) :~/CHATBOT$
```

## 4. Running the Streamlit Application

#### 4.1. Prerequisites

- Python (version 3.7 or later)

#### 4.2. Environment setup

- Create a virtual environment

```bash
(base) :~/CHATBOT$ python -m venv venv
```

- Activate the environment using the below command

```bash
(base) :~/CHATBOT$ source venv/bin/activate
(.venv) (base) :~/CHATBOT$
```

- Install the requirements

```bash
(.venv) (base) :~/CHATBOT$ pip install -r env/requirements.txt
```

#### 4.3. Command to run the Application

```bash
(.venv) (base) :~/CHATBOT$ streamlit run chatbot2.py
```

#### 4.6. View the Application

- Open "localhost:8051" in your browser

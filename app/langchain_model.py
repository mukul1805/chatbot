from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
api_key = os.getenv('OPENAI_API_KEY')


llm = OpenAI(model="gpt-3.5-turbo", openai_api_key=api_key)

# Prompt-template 
template = """ Given the following text, please answer the question.
            Text: {text}
            Question: {question}
            Answer:
            """

prompt = PromptTemplate(input_variables=["text", "question"], template=template)

def extract_answer(text: str, question: str) -> str:
    prompt_text = prompt.format(text=text, question=question)
    return llm.invoke(prompt_text)

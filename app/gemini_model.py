import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY') 
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

def extract_answer_with_gemini(text: str, question: str) -> str:
    prompt_text = f"Given the following text, please answer the question:\nText: {text}\nQuestion: {question}"

    try:
        response = model.generate_content(prompt_text)
        answer = response.text
        return answer
    except Exception as e:
        raise Exception(f"Error using Gemini model: {str(e)}")
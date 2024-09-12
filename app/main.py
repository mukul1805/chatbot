from fastapi import FastAPI, HTTPException , UploadFile, File, Form
from PyPDF2 import PdfReader
from .langchain_model import extract_answer
from . import schemas

app=FastAPI()

# pdf_path = "gpt-4.pdf"

def extract_text_from_pdf(pdf_file) -> str:
    try:
        reader = PdfReader(pdf_file)
        pdf_text = ""
        # for page in reader.pages:
        #     pdf_text += page.extract_text()
        pdf_text += reader.pages[0].extract_text()
        return pdf_text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading PDF: {str(e)}")


# @app.get('/get')
# def get_data_from_pdf():
#     return (extract_text_from_pdf())


@app.post("/extract-answer/")
async def extract_answer_from_pdf( file: UploadFile = File(...), question: str = Form(...)):
    pdf_text = extract_text_from_pdf(file.file)
    answer = extract_answer(pdf_text, question)
    return {"question": question, "answer": answer}


@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    # Extract text from the uploaded PDF
    pdf_text = extract_text_from_pdf(file.file)
    return {"pdf_text": pdf_text}
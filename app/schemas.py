from pydantic import BaseModel
from fastapi import Form

# class QARequest(BaseModel):
#     # text: str
#     question: str


# Update the schema to handle form data
class QARequest:
    def __init__(self, question: str = Form(...)):
        self.question = question
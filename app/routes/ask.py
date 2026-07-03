from fastapi import APIRouter
from app.models.ask_model import AskRequest
from app.services.ask_service import ask_question

router = APIRouter()

@router.post("/ask")
def ask(request: AskRequest):

    return ask_question(request.question)
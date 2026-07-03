from fastapi import APIRouter
from app.models.query_model import QueryRequest
from app.services.query_service import execute_query

router = APIRouter()

@router.post("/query")
def query(request: QueryRequest):

    return execute_query(request.query)
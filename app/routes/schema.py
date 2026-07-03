from fastapi import APIRouter
from app.services.schema_service import get_schema

router = APIRouter()

@router.get("/schema")
def schema():
    return get_schema()
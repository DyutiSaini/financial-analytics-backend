from fastapi import APIRouter
from app.services.metadata_service import get_metadata

router = APIRouter()

@router.get("/metadata")
def metadata():

    return get_metadata()
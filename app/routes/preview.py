from fastapi import APIRouter
from app.services.file_service import get_preview

router = APIRouter()


@router.get("/preview")
def preview_file():

    result = get_preview()

    return result

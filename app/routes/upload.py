from fastapi import APIRouter, UploadFile, File
from app.services.file_service import save_uploaded_file

router = APIRouter()


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    result = save_uploaded_file(file)

    return result
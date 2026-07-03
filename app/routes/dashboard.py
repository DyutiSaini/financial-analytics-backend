from fastapi import APIRouter
from app.services.dashboard_service import get_dashboard

router = APIRouter()

@router.get("/dashboard")
def dashboard():

    return get_dashboard()
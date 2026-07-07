from fastapi import FastAPI
from app.routes.upload import router as upload_router
from app.routes.preview import router as preview_router
from app.routes.metadata import router as metadata_router
from app.routes.dashboard import router as dashboard_router
from app.routes.schema import router as schema_router
from app.routes.query import router as query_router
from app.routes.ask import router as ask_router
from app.routes.analysis import router as analysis_router

app = FastAPI(
    title="Financial Analytics Backend",
    version="1.0.0"
)

app.include_router(analysis_router)
app.include_router(dashboard_router)

app.include_router(metadata_router)
app.include_router(query_router)
app.include_router(ask_router)

app.include_router(preview_router)

app.include_router(schema_router)

app.include_router(upload_router)


@app.get("/")
def home():
    return {
        "message": "Financial Analytics Backend is Running Successfully!"
    }
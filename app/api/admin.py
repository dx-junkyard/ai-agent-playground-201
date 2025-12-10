from fastapi import FastAPI, HTTPException, Request
from typing import Dict, Any, List
from app.api.db import DBClient
import logging

app = FastAPI()

# ログ設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.delete("/api/v1/service-catalog/reset")
async def reset_catalog():
    repo = DBClient()
    if repo.truncate_service_catalog():
         # Also reset Qdrant if possible, but for now just DB
         return {"status": "success", "message": "Service catalog reset."}
    raise HTTPException(status_code=500, detail="Failed to reset catalog")

@app.post("/api/v1/service-catalog/import")
async def import_catalog(request: Request):
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON")

    # Minimal implementation to prevent crash
    repo = DBClient()
    repo.create_service_catalog_table()

    count = 0
    if isinstance(data, list):
        for item in data:
            repo.insert_service_catalog_entry(item)
            count += 1

    return {"status": "success", "imported_count": count}

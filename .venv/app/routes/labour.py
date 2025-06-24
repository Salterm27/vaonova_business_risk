from fastapi import APIRouter, HTTPException
from app.utils.NAICS_OpenAI import fetch_naics_code

router = APIRouter()

@router.post("/naics/{business_category}/")
def get_naics_code(business_category: str):
    try:
        result = fetch_naics_code(business_category)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
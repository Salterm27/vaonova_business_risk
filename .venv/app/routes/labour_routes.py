from fastapi import APIRouter, HTTPException
from app.utils.NAICS_OpenAI import get_naics_from_db, fetch_naics_code_from_gpt, save_naics_to_db

router = APIRouter()

@router.post("/naics/{business_category}/")
async def get_naics_code(business_category: str):
    try:
        # 1. Try DB first
        db_result = await get_naics_from_db(business_category)
        if db_result:
            return {
                "naics_code": db_result["code"],
                "description": db_result["description"]
            }

        # 2. Fallback to OpenAI
        gpt_result = fetch_naics_code_from_gpt(business_category)

        # 3. Save to DB
        await save_naics_to_db(
            category=business_category,
            code=gpt_result["code"],
            description=gpt_result["description"]
        )

        return {
            "naics_code": gpt_result["code"],
            "description": gpt_result["description"]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

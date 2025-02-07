from fastapi import UploadFile, File,APIRouter
from backend.utils import hr_extract

#creating router instance
router=APIRouter()

#route for extracting skills from hr job description
@router.post("/extract_hr_skills")
async def extract_skills(file:UploadFile=File(...)):
    return hr_extract.extract_hr_skills(file)
from fastapi import APIRouter,UploadFile,File
from backend.utils import resume_extract


#creating router instanace
router=APIRouter()


#route for extracting resume contents
@router.post("/extract-resume-entities")
async def extract_resume(file:UploadFile=File(...)):
    return resume_extract.generate_response(file)
from fastapi import FastAPI ,Depends
from typing import Annotated
from utils.auth import get_current_user
from fastapi.middleware.cors import CORSMiddleware
from routers import  user_router,personalInfo_router,workExperience_router,skill_router,technical_router,softskill_router,skillnameMapping_router,proficiencyMapping_router,skillname_router,proficiency_router,auth_router
from utils.auth import get_current_user

app = FastAPI(
    title="Fast API"
)
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router.router, tags=["auth"])
app.include_router(user_router.router, tags=["user"],dependencies=[Depends(get_current_user)])
app.include_router(personalInfo_router.router, tags=["personalInfo"],dependencies=[Depends(get_current_user)])
app.include_router(workExperience_router.router, tags=["workExperience"],dependencies=[Depends(get_current_user)])
app.include_router(skill_router.router, tags=["skill"],dependencies=[Depends(get_current_user)])
app.include_router(technical_router.router, tags=["technical"],dependencies=[Depends(get_current_user)])
app.include_router(softskill_router.router, tags=["softskill"],dependencies=[Depends(get_current_user)])
app.include_router(skillnameMapping_router.router, tags=["skillnameMapping"],dependencies=[Depends(get_current_user)])
app.include_router(proficiencyMapping_router.router, tags=["proficiencyMapping"],dependencies=[Depends(get_current_user)])
app.include_router(skillname_router.router, tags=["skillname"],dependencies=[Depends(get_current_user)])
app.include_router(proficiency_router.router, tags=["proficiency"],dependencies=[Depends(get_current_user)])

# myenv\Scripts\activate
#  python -m uvicorn main:app --reload


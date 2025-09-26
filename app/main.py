from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from routers import  user_router,personalInfo_router,workExperience_router,skill_router,technical_router,softskill_router,skillnameMapping_router,proficiencyMapping_router,skillname_router,proficiency_router
 
app = FastAPI(
    title="Fast API",
    version="1.0.0"
)
 


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router.router, tags=["user"])
app.include_router(personalInfo_router.router, tags=["personalInfo"])
app.include_router(workExperience_router.router, tags=["workExperience"])
app.include_router(skill_router.router, tags=["skill"])
app.include_router(technical_router.router, tags=["technical"])
app.include_router(softskill_router.router, tags=["softskill"])
app.include_router(skillnameMapping_router.router, tags=["skillnameMapping"])
app.include_router(proficiencyMapping_router.router, tags=["proficiencyMapping"])
app.include_router(skillname_router.router, tags=["skillname"])
app.include_router(proficiency_router.router, tags=["proficiency"])

# myenv\Scripts\activate
#  python -m uvicorn main:app --reload


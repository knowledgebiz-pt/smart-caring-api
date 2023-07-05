import os

import uvicorn
from fastapi import FastAPI, Depends
import internal
from fastapi.middleware.cors import CORSMiddleware
import routers

app = FastAPI(
    contact=dict(
        email="geral@knowldgzebiz.pt",
        http="https://knowledgebiz.pt"
    ),
    version="1.0.9",
    title="API SMART CARING",
    description="This API integrates with SMART CARING system",
    #root_path="https://smart-caring.azurewebsites.net/"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
app.include_router(routers.user_router.router, prefix="/user", tags=["user"])
app.include_router(routers.news_router.router, prefix="/news", tags=["news"], dependencies=[Depends(internal.auth.JwtBearer())])
app.include_router(routers.likes_router.router, prefix="/likes", tags=["likes"], deprecated=True)
app.include_router(routers.toolbox_router.router, prefix="/toolbox", tags=["toolbox"])
app.include_router(routers.schedule_router.router, prefix="/schedule", tags=["schedule"])
app.include_router(routers.comment_router.router, prefix="/comment", tags=["comment"])
app.include_router(routers.diary_router.router, prefix="/diary", tags=["diary"])
app.include_router(routers.jwt_router.router, prefix="/jwt", tags=["jwt"])
app.include_router(routers.chat_router.router, prefix="/chat", tags=["chat"])
app.include_router(routers.group_router.router, prefix="/groups", tags=["groups"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

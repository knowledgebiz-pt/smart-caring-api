import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import routers

app = FastAPI(
    contact=dict(
        email="geral@knowldgzebiz.pt",
        http="https://knowledgebiz.pt"
    ),
    version="1.0.3",
    title="API SMART CARING",
    description="This API integrates with SMART CARING system"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
app.include_router(routers.user_router.router, prefix="/user", tags=["user"])
app.include_router(routers.news_router.router, prefix="/news", tags=["news"])
app.include_router(routers.likes_router.router, prefix="/likes", tags=["likes"])
app.include_router(routers.toolbox_router.router, prefix="/toolbox", tags=["toolbox"])
app.include_router(routers.schedule_router.router, prefix="/schedule", tags=["schedule"])
app.include_router(routers.diary_router.router, prefix="/diary", tags=["diary"])
app.include_router(routers.jwt_router.router, prefix="/jwt", tags=["jwt"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=2828)

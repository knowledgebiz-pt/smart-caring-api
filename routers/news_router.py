from fastapi import APIRouter, HTTPException, Response, status
import core.schemes
import database.news_database

router = APIRouter()


@router.post("/",
             summary="Creates a new news article",
             description="Creates a new news article",
             response_description="Creates a new news article",
             response_model=core.schemes.news_schemes.NewsCreateResponse,
             operation_id="CreateNews"
             )
async def create_news(article: core.schemes.news_schemes.NewsPost):
    response = database.news_database.add_news(article)
    return {"msg": "success",
            "data": {response}}

@router.get("/by-id/{id_news}",
             summary="Return news article by id_news",
             description="Return news article by id_news",
             response_description="Return news article by its ID",
             response_model=core.schemes.news_schemes.NewsGetResponse,
             operation_id="GetNewsArticleByIdNews"
            )
async def get_by_id(response: Response, id_news: str):
    response_database = database.news_database.return_news_by_id(id_news)
    if response_database is None or not response_database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "Article not found."}
    else:
        return {
            "msg": "success",
            "data": response_database
            }

@router.get("/by-user-id/{id_user}",
            summary= "Return news articles by id_user",
            description= "Return news articles by id_user",
            response_description="Return news articles from user",
            response_model= core.schemes.news_schemes.NewsGetResponse,
            operation_id="GetNewsArticlesByIdUser"
            )
async def get_by_id_user(response: Response, id_user: str):
    response_database = database.news_database.return_news_by_user_id(id_user)
    if response_database is None or not response_database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "No articles found for this user"}
    else:
        return {"msg": "success",
            "data": response_database}

@router.delete("/by-id/{id_news}",
               summary="Delete news article by id_news",
               description="Delete news article by id_news",
               response_description="Delete news article by its ID",
               response_model=core.schemes.news_schemes.NewsDeleteResponse,
               operation_id="DeleteNewsArticleByIdNews"
               )
async def delete_by_id(response: Response, id_news: str):
    response_database = database.news_database.delete_news_by_id(id_news)
    return {"msg": "success", "data": []}
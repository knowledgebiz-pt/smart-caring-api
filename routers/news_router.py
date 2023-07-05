from fastapi import APIRouter, HTTPException, Response, status, Depends
import core.schemes
import database.news_database
import internal.merge_news_user

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
    if response is None or not response:
        return {"msg": "error", "data": "Article not created."}
    else:
        return {"msg": "success", "data": response}


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
            summary="Return news articles by id_user",
            description="Return news articles by id_user",
            response_description="Return news articles from user",
            response_model=core.schemes.news_schemes.NewsGetResponse,
            operation_id="GetNewsArticlesByIdUser"
            )
async def get_by_id_user(response: Response, id_user: str):
    response_database = database.news_database.return_news_by_user_id(id_user)
    if response_database is None or not response_database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "No articles found for this user"}
    else:
        return {"msg": "success", "data": response_database}


@router.get("/",
            summary="Return all news articles",
            description="Return all news articles",
            response_description="Return all news articles",
            response_model=core.schemes.news_schemes.NewsGetResponse,
            operation_id="GetNewsAllArticles"
            )
async def get_by_id_user(response: Response):
    response_news = database.news_database.return_all_news()
    response_users = database.user_database.return_all_users()
    response_news_merged = internal.merge_news_user.merge_news_user(response_news, response_users)
    if response_news is None or not response_news:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "No articles found"}
    else:
        return {"msg": "success", "data": response_news_merged}


@router.post("/add-like/",
             summary="Add like to news article",
             description="Add like to news article",
             response_description="Add like to news article",
             response_model=core.schemes.news_schemes.NewsCreateResponse,
             operation_id="AddLikeToNewsArticle"
             )
async def add_like(response: Response, id_news: str, id_user: str):
    response_database = database.news_database.add_like_in_news(id_news, id_user)
    if response_database is None or not response_database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "Article not found."}
    else:
        return {"msg": "success", "data": response_database}


@router.delete("/delete-like/",
               summary="Delete like to news article",
               description="Delete like to news article",
               response_description="Delete like to news article",
               response_model=core.schemes.news_schemes.NewsCreateResponse,
               operation_id="DeleteLikeToNewsArticle"
               )
async def delete_like(response: Response, id_news: str, id_user: str):
    response_database = database.news_database.delete_like_in_news(id_news, id_user)
    if response_database is None or not response_database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "Article not found."}
    else:
        return {"msg": "success", "data": response_database}


@router.post("/add-favorites/",
             summary="Add favorites to news article",
             description="Add favorites to news article",
             response_description="Add favorites to news article",
             response_model=core.schemes.news_schemes.NewsCreateResponse,
             operation_id="AddFavoritesToNewsArticle"
             )
async def add_favorites(response: Response, id_news: str, id_user: str):
    response_database = database.news_database.add_favorite_in_news(id_news, id_user)
    if response_database is None or not response_database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "Article not found."}
    else:
        return {"msg": "success", "data": response_database}


@router.delete("/delete-favorites/",
               summary="Delete favorites to news article",
               description="Delete favorites to news article",
               response_description="Delete favorites to news article",
               response_model=core.schemes.news_schemes.NewsCreateResponse,
               operation_id="DeleteFavoritesToNewsArticle"
               )
async def delete_favorites(response: Response, id_news: str, id_user: str):
    response_database = database.news_database.delete_favorite_in_news(id_news, id_user)
    if response_database is None or not response_database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "Article not found."}
    else:
        return {"msg": "success", "data": response_database}


@router.delete("/by-id/{id_news}",
               summary="Delete news article by id_news",
               description="Delete news article by id_news",
               response_description="Delete news article by its ID",
               response_model=core.schemes.news_schemes.NewsDeleteResponse,
               operation_id="DeleteNewsArticleByIdNews"
               )
async def delete_by_id(response: Response, id_news: str):
    database.news_database.delete_news_by_id(id_news)
    return {"msg": "success", "data": "Deleted article."}

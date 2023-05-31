from fastapi import APIRouter, HTTPException, Response, status
import core.schemes
import database.likes_database

router = APIRouter()


@router.post("/",
             summary="Creates a new like",
             description="Creates a new like",
             response_description="Creates a new like",
             response_model=core.schemes.likes_scheme.LikesCreateResponse,
             operation_id="CreateLike"
             )
async def create_news(like: core.schemes.likes_scheme.LikesPost):
    response = database.likes_database.add_like(like)
    return {"msg": "success",
            "data": {response}}

@router.get("/by-news-id/{id_news}",
             summary="Return likes by id_news",
             description="Return likes by id_news",
             response_description="Return a news articles' likes",
             response_model=core.schemes.likes_scheme.LikesGetResponse,
             operation_id="GetLikesByIdNews"
            )
async def get_by_id(response: Response, id_news: str):
    response_database = database.likes_database.return_likes_by_id_news(id_news)
    if response_database is None or not response_database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "No likes found for specified article."}
    else:
        return {
            "msg": "success",
            "data": response_database
            }

@router.get("/by-user-id/{id_user}",
            summary= "Return likes by id_user",
            description= "Return likes by id_user",
            response_description="Return likes from user",
            response_model= core.schemes.likes_scheme.LikesGetResponse,
            operation_id="GetLikesByIdUser"
            )
async def get_by_id_user(response: Response, id_user: str):
    response_database = database.likes_database.return_likes_by_user_id(id_user)
    if response_database is None or not response_database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "No likes found from this user"}
    else:
        return {"msg": "success",
            "data": response_database}

@router.delete("/by-id/{id_likes}",
               summary="Delete like by id_likes",
               description="Delete like by id_likes",
               response_description="Delete like by its ID",
               response_model=core.schemes.likes_scheme.LikesDeleteResponse,
               operation_id="DeleteLikeByIdLikes"
               )
async def delete_by_id(response: Response, id_likes: str):
    response_database = database.likes_database.delete_likes_by_id(id_likes)
    return {"msg": "success", "data": []}
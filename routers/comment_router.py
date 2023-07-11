from fastapi import APIRouter, HTTPException, Response, status
import core.schemes
import database.comment_database
import database.user_database

router = APIRouter()


@router.post("/",
             summary="Creates a new comment",
             description="Creates a new comment",
             response_description="Creates a new comment",
             response_model=core.schemes.comment_schemes.CommentCreateResponse,
             operation_id="CreateComment"
             )
async def create_comment(like: core.schemes.comment_schemes.CommentPost):
    response = database.comment_database.add_comment(like)
    return {"msg": "success",
            "data": response}

@router.get("/by-comment-id/{id_comment}",
             summary="Return comments by id_comment",
             description="Return comments by id_comment",
             response_description="Return a comment",
             response_model=core.schemes.comment_schemes.CommentGetResponse,
             operation_id="GetCommentByIdComment"
            )
async def get_by_id(response: Response, id_comment: str):
    response_database = database.comment_database.return_comments_by_id(id_comment)
    users = database.user_database.return_all_users()
    for item in response_database:
        for user in users:
            if item["user_id"] == user["_id"]["$oid"]:
                user_info = {
                    "user_name": user["name"],
                    "user_type": user["user_type"],
                    "user_picture": user["picture"]
                }
                if users is not None:
                    item["user_info"] = user_info
    if response_database is None or not response_database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "No comment found for comment ID"}
    else:
        return {
            "msg": "success",
            "data": response_database
            }

@router.get("/by-news-id/{id_news}",
             summary="Return comments by id_news",
             description="Return comments by id_news",
             response_description="Return a news articles' comments",
             response_model=core.schemes.comment_schemes.CommentGetResponse,
             operation_id="GetCommentsByIdNews"
            )
async def get_by_id(response: Response, id_news: str):
    response_database = database.comment_database.return_comments_by_id_news(id_news)
    users = database.user_database.return_all_users()
    for item in response_database:
        for user in users:
            if item["user_id"] == user["_id"]["$oid"]:
                user_info = {
                    "user_name": user["name"],
                    "user_type": user["user_type"],
                    "user_picture": user["picture"]
                }
                if users is not None:
                    item["user_info"] = user_info
    if response_database is None or not response_database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "No comments found for specified article."}
    else:
        return {
            "msg": "success",
            "data": response_database
            }

@router.get("/by-user-id/{id_user}",
            summary= "Return comments by id_user",
            description= "Return comments by id_user",
            response_description="Return comments from user",
            response_model= core.schemes.comment_schemes.CommentGetResponse,
            operation_id="GetCommentsByIdUser"
            )
async def get_by_id_user(response: Response, id_user: str):
    response_database = database.comment_database.return_comments_by_user_id(id_user)
    users = database.user_database.return_all_users()
    for item in response_database:
        for user in users:
            if item["user_id"] == user["_id"]["$oid"]:
                user_info = {
                    "user_name": user["name"],
                    "user_type": user["user_type"],
                    "user_picture": user["picture"],
                    "visibility": user["visibility"]
                }
                if users is not None:
                    item["user_info"] = user_info
    if response_database is None or not response_database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "No comments found from this user"}
    else:
        return {"msg": "success",
            "data": response_database}

@router.delete("/by-id/{id_comment}",
               summary="Delete comment by id_comment",
               description="Delete comment by id_comment",
               response_description="Delete comment by its ID",
               response_model=core.schemes.comment_schemes.CommentDeleteResponse,
               operation_id="DeleteCommentByIdComment"
               )
async def delete_by_id(response: Response, id_comment: str):
    response_database = database.comment_database.delete_comment_by_id(id_comment)
    return {"msg": "success", "data": []}

@router.delete("/by-news-id/{id_news}",
               summary="Delete comments by id_news",
               description="Delete comments by id_news",
               response_description="Delete comments by news' post ID",
               response_model=core.schemes.comment_schemes.CommentDeleteResponse,
               operation_id="DeleteCommentByIdNews"
               )
async def delete_by_id(response: Response, id_news: str):
    response_database = database.comment_database.delete_comments_by_id_news(id_news)
    return {"msg": "success", "data": []}
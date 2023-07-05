from fastapi import APIRouter, HTTPException, Response, status
import core.schemes
import database.chat_database

router = APIRouter()


@router.post("/",
             summary="Creates a new chat entry",
             description="Creates a new chat entry",
             response_description="Creates a new chat",
             response_model=core.schemes.chat_schemes.ChatCreateResponse,
             operation_id="CreateChat"
             )
async def create_chat(entry: core.schemes.chat_schemes.ChatPost):
    response = database.chat_database.add_chat(entry)
    return {"msg": "success",
            "data": {response}}

@router.get("/by-id/{id_chat}",
             summary="Return chat by id_chat",
             description="Return chat by id_chat",
             response_description="Return chat by its ID",
             response_model=core.schemes.chat_schemes.ChatGetResponse,
             operation_id="GetChatByIdChat"
            )
async def get_by_id(response: Response, id_chat: str):
    response_database = database.chat_database.return_chat_by_id(id_chat)
    if response_database is None or not response_database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "Chat not found."}
    else:
        return {
            "msg": "success",
            "data": response_database
            }

@router.get("/by-user-id/{id_user}",
            summary= "Return chat by id_user",
            description= "Return chat by id_user",
            response_description="Return chat from user",
            response_model= core.schemes.chat_schemes.ChatGetResponse,
            operation_id="GetChatByIdUser"
            )
async def get_by_id_user(response: Response, id_user: str):
    response_database = database.chat_database.return_chat_by_user_id(id_user)
    if response_database is None or not response_database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "No chat found for this user"}
    else:
        return {"msg": "success",
            "data": response_database}

@router.delete("/by-id/{id_chat}",
               summary="Delete chat by id chat",
               description="Delete chat by id chat",
               response_description="Delete chat by its ID",
               response_model=core.schemes.chat_schemes.ChatDeleteResponse,
               operation_id="DeleteChatByIdNews"
               )
async def delete_by_id(response: Response, id_chat: str):
    response_database = database.chat_database.delete_chat_by_id(id_chat)
    return {"msg": "success", "data": []}
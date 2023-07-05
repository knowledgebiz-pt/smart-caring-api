from fastapi import APIRouter, HTTPException, Response, status
import core.schemes
import database.group_database

router = APIRouter()


@router.post("/",
             summary="Creates a new group entry",
             description="Creates a new group entry",
             response_description="Creates a new group",
             response_model=core.schemes.group_schemes.GroupCreateResponse,
             operation_id="CreateGroup"
             )
async def create_group(entry: core.schemes.group_schemes.GroupPost):
    response = database.group_database.add_group(entry)
    return {"msg": "success",
            "data": {response}}

@router.get("/by-id/{id_group}",
             summary="Return group by id_group",
             description="Return group by id_group",
             response_description="Return group by its ID",
             response_model=core.schemes.group_schemes.GroupGetResponse,
             operation_id="GetGroupByIdGroup"
            )
async def get_by_id(response: Response, id_group: str):
    response_database = database.group_database.return_group_by_id(id_group)
    if response_database is None or not response_database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "Group not found."}
    else:
        return {
            "msg": "success",
            "data": response_database
            }

@router.get("/by-user-id/{id_user}",
            summary= "Return group by id_user",
            description= "Return group by id_user",
            response_description="Return group from user",
            response_model= core.schemes.group_schemes.GroupGetResponse,
            operation_id="GetGroupByIdUser"
            )
async def get_by_id_user(response: Response, id_user: str):
    response_database = database.group_database.return_group_by_user_id(id_user)
    if response_database is None or not response_database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "No group found for this user"}
    else:
        return {"msg": "success",
            "data": response_database}

@router.delete("/by-id/{id_group}",
               summary="Delete group by id group",
               description="Delete group by id group",
               response_description="Delete group by its ID",
               response_model=core.schemes.group_schemes.GroupDeleteResponse,
               operation_id="DeleteGroupByIdNews"
               )
async def delete_by_id(response: Response, id_group: str):
    response_database = database.group_database.delete_group_by_id(id_group)
    return {"msg": "success", "data": []}
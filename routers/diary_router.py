from fastapi import APIRouter, HTTPException, Response, status
import core.schemes
import database.diary_database

router = APIRouter()


@router.post("/",
             summary="Creates a new diary entry",
             description="Creates a new diary entry",
             response_description="Creates a new diary",
             response_model=core.schemes.diary_schemes.DiaryCreateResponse,
             operation_id="CreateDiary"
             )
async def create_diary(entry: core.schemes.diary_schemes.DiaryPost):
    response = database.diary_database.add_diary(entry)
    return {"msg": "success",
            "data": {response}}

@router.get("/by-id/{id_diary}",
             summary="Return diary by id_diary",
             description="Return diary by id_diary",
             response_description="Return diary by its ID",
             response_model=core.schemes.diary_schemes.DiaryGetResponse,
             operation_id="GetDiaryByIdDiary"
            )
async def get_by_id(response: Response, id_diary: str):
    response_database = database.diary_database.return_diary_by_id(id_diary)
    if response_database is None or not response_database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "Diary not found."}
    else:
        return {
            "msg": "success",
            "data": response_database
            }

@router.get("/by-user-id/{id_user}",
            summary= "Return diary by id_user",
            description= "Return diary by id_user",
            response_description="Return diary from user",
            response_model= core.schemes.diary_schemes.DiaryGetResponse,
            operation_id="GetDiaryByIdUser"
            )
async def get_by_id_user(response: Response, id_user: str):
    response_database = database.diary_database.return_diary_by_user_id(id_user)
    if response_database is None or not response_database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "No diary found for this user"}
    else:
        return {"msg": "success",
            "data": response_database}

@router.delete("/by-id/{id_diary}",
               summary="Delete diary by id diary",
               description="Delete diary by id diary",
               response_description="Delete diary by its ID",
               response_model=core.schemes.diary_schemes.DiaryDeleteResponse,
               operation_id="DeleteDiaryByIdNews"
               )
async def delete_by_id(response: Response, id_diary: str):
    response_database = database.diary_database.delete_diary_by_id(id_diary)
    return {"msg": "success", "data": []}
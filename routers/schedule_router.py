from fastapi import APIRouter, HTTPException, Response, status
import core.schemes
import database.schedule_database

router = APIRouter()


@router.post("/",
             summary="Creates a new schedule event",
             description="Creates a new schedule event",
             response_description="Creates a new schedule event",
             response_model=core.schemes.schedule_schemes.ScheduleCreateResponse,
             operation_id="CreateSchedule"
             )
async def create_schedule(event: core.schemes.schedule_schemes.SchedulePost):
    response = database.schedule_database.add_schedule(event)
    return {"msg": "success",
            "data": {response}}

@router.get("/by-id/{id_schedule}",
             summary="Return schedule event by id_schedule",
             description="Return schedule event by id_schedule",
             response_description="Return schedule event by its ID",
             response_model=core.schemes.schedule_schemes.ScheduleGetResponse,
             operation_id="GetScheduleArticleByIdSchedule"
            )
async def get_by_id(response: Response, id_schedule: str):
    response_database = database.schedule_database.return_schedule_by_id(id_schedule)
    if response_database is None or not response_database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "Schedule event not found."}
    else:
        return {
            "msg": "success",
            "data": response_database
            }

@router.get("/by-user-id/{id_user}",
            summary= "Return schedule events by id_user",
            description= "Return schedule events by id_user",
            response_description="Return schedule events from user",
            response_model= core.schemes.schedule_schemes.ScheduleGetResponse,
            operation_id="GetScheduleEventByIdUser"
            )
async def get_by_id_user(response: Response, id_user: str):
    response_database = database.schedule_database.return_schedule_by_user_id(id_user)
    if response_database is None or not response_database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "No Event found for this user"}
    else:
        return {"msg": "success",
            "data": response_database}

@router.delete("/by-id/{id_schedule}",
               summary="Delete schedule event by id_schedule",
               description="Delete schedule event by id_schedule",
               response_description="Delete schedule event by its ID",
               response_model=core.schemes.schedule_schemes.ScheduleDeleteResponse,
               operation_id="DeleteScheduleArticleByIdSchedule"
               )
async def delete_by_id(response: Response, id_schedule: str):
    response_database = database.schedule_database.delete_schedule_by_id(id_schedule)
    return {"msg": "success", "data": []}
from fastapi import APIRouter, HTTPException, Response, status
import core.schemes
import database.user_database

router = APIRouter()


@router.post("/by-id/{id_user}",
             summary="Creates a new user by id_user",
             description="Creates a new user by id_user",
             response_description="Creates a new user",
             response_model=core.schemes.user_schemes.UserCreateResponse,
             operation_id="CreateUserByIdUser"
             )
async def create_user(user: core.schemes.user_schemes.UserPost):
    response = database.user_database.add_user(user)
    return {"msg": "success",
            "data": {response}}


@router.get("/by-id/{email}/{password}",
            summary= "Return user data by email and password",
            description= "Return data of user by email and password",
            response_model= core.schemes.user_schemes.UserGetResponse,
            operation_id="GetUserDataByIdUser"
            )
async def service(response: Response, email: str, password: str):
    response_database = database.user_database.return_user_by_email_and_password(email, password)
    if response_database is None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"msg": "error", "data": "This User does not exist"}
    else:
        return {"msg": "success",
            "data": response_database}
import datetime
from internal import send_email
from fastapi import APIRouter, HTTPException, Response, status
import core.schemes
import database.user_database
import internal

router = APIRouter()


@router.post("",
             summary="Creates a new user",
             description="Creates a new user",
             response_description="Creates a new user",
             response_model=core.schemes.user_schemes.UserCreateResponse,
             operation_id="CreateUser"
             )
async def create_user(user: core.schemes.user_schemes.UserPost):
    response = database.user_database.add_user(user)
    return {"msg": "success",
            "data": {response}}


@router.get("/by-id/{email}/{password}",
            summary="Return user data by email and password",
            description="Return data of user by email and password",
            response_model=core.schemes.user_schemes.UserGetResponse,
            operation_id="GetUserDataByIdUser"
            )
async def service(response: Response, email: str, password: str):
    response_database = database.user_database.return_user_by_email_and_password(email, password)
    if response_database is None or not response_database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "This User does not exist"}
    else:
        return {"msg": "success",
                "data": response_database}


@router.get("/recover-password-by-email/{email}",
            summary="Recover password by email",
            description="Recover password by email",
            response_model=core.schemes.user_schemes.UserGetResponse,
            operation_id="RecoverUserPassword"
            )
async def service(response: Response, email: str):
    response_database = database.user_database.return_user_by_email(email)
    if response_database is None or not response_database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "This User does not exist"}
    else:
        recover_message = database.user_database.add_recover_password(response_database)
        send_email.send_recovery_code(recover_message)
        return {"msg": "success",
                "data": response_database}


@router.get("/verify-recovery-code/{email}",
            summary="Verifies if code is valid",
            description="Verifies if code is valid",
            response_model=core.schemes.user_schemes.UserGetResponse,
            operation_id="VerifiesRecoveryCode"
            )
async def service(response: Response, email: str, code: str):
    code = database.user_database.return_verify_email_and_code(email, code)
    if code is not None:
        response_code_verifications = internal.verify_code.diff_between_time(datetime.datetime.now(), code["created"])
        if response_code_verifications is True:
            return {"msg": "success",
                    "data": "Change password permitted"}
        else:
            return {"msg": "error",
                    "data": "Invalid code"}
    else:
        print("HERE")


@router.put("update-password/{email}/{password}",
            summary="Updates user password",
            description="Updates user password",
            response_model=core.schemes.user_schemes.UserUpdatePasswordResponse,
            operation_id="UpdateUserPassword"
            )
async def service(response: Response,email: str, password: str):
    response_database = database.user_database.update_user_password(email, password)
    if response_database is False:
        return {"msg": "error", "data": "Password change failed"}
    else:
        return {"msg": "success",
                "data": response_database}

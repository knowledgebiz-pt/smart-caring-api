from fastapi import APIRouter, HTTPException, Response, status
import core.schemes
import database.toolbox_database

router = APIRouter()

@router.get("/by-id/{id_toolbox}",
             summary="Return Tool Box by id_toolbox",
             description="Return Tool Box by id_toolbox",
             response_description="Return Tool Box by its ID",
             response_model=core.schemes.toolbox_schemes.ToolBoxGetResponse,
             operation_id="GetToolBoxByIdToolbox"
            )
async def get_by_id(response: Response, id_toolbox: str):
    response_database = database.toolbox_database.return_toolbox_by_id(id_toolbox)
    if response_database is None or not response_database:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"msg": "error", "data": "Article not found."}
    else:
        return {
            "msg": "success",
            "data": response_database
            }
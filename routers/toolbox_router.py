from fastapi import APIRouter, HTTPException, Response, status
import core.schemes
import database.toolbox_database

router = APIRouter()


@router.post("/",
             summary="Creates a new Tool Box",
             description="Creates a new Tool Box",
             response_description="Creates a new Tool Box",
             response_model=core.schemes.toolbox_schemes.ToolBoxGetResponse,
             operation_id="CreateToolBox"
             )
async def create_toolbox(tool: core.schemes.toolbox_schemes.ToolBoxPost):
    response = database.toolbox_database.add_toolbox(tool)
    return {"msg": "success",
            "data": {response}}

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

@router.delete("/by-id/{id_toolbox}",
               summary="Delete Tool Box by id_toolbox",
               description="Delete Tool Box by id_toolbox",
               response_description="Delete Tool Box by its ID",
               response_model=core.schemes.toolbox_schemes.ToolBoxDeleteResponse,
               operation_id="DeleteToolboxByIdToolBox"
               )
async def delete_by_id(response: Response, id_toolbox: str):
    response_database = database.toolbox_database.delete_toolbox_by_id(id_toolbox)
    return {"msg": "success", "data": []}
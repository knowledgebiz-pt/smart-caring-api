from fastapi import APIRouter, HTTPException, Response, status, Depends
import core.schemes
import internal.requests_shapes

router = APIRouter()


@router.get("/",
            summary="Return all products from SHAPES",
            description="Return all products from SHAPES",
            response_description="Return all products from SHAPES",
            response_model=core.schemes.toolbox_schemes.ToolBoxGetResponse,
            operation_id="GetToolBoxAllProducts",
            dependencies=[Depends(internal.auth.JwtBearer())]
            )
async def get_by_id(response: Response):
    response = internal.requests_shapes.get_all_products()

    return {"msg": "success", "data": {
        "items": response["data"]["items"],
        "total_products": len(response["data"]["items"])
    }}

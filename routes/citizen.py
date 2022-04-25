from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from database.database import *
from models.citizen import *

router = APIRouter()


@router.get("/", response_description="citizens retrieved")
async def get_citizens():
    citizens = await retrieve_citizens()
    return ResponseModel(citizens, "citizens data retrieved successfully") \
        if len(citizens) > 0 \
        else ResponseModel(
        citizens, "Empty list returned")


@router.get("/{id}", response_description="citizen data retrieved")
async def get_citizen_data(id):
    citizen = await retrieve_citizen(id)
    return ResponseModel(citizen, "citizen data retrieved successfully") \
        if citizen \
        else ErrorResponseModel("An error occured.", 404, "citizen doesn't exist.")


@router.post("/", response_description="citizen data added into the database")
async def add_citizen_data(citizen: CitizenModel = Body(...)):
    citizen = jsonable_encoder(citizen)
    new_citizen = await add_citizen(citizen)
    return ResponseModel(new_citizen, "citizen added successfully.")


@router.delete("/{id}", response_description="citizen data deleted from the database")
async def delete_citizen_data(id: str):
    deleted_citizen = await delete_citizen(id)
    return ResponseModel("citizen with ID: {} removed".format(id), "citizen deleted successfully") \
        if deleted_citizen \
        else ErrorResponseModel("An error occured", 404, "citizen with id {0} doesn't exist".format(id))


@router.put("{id}")
async def update_citizen(id: str, req: UpdateCitizenModel = Body(...)):
    updated_citizen = await update_citizen_data(id, req.dict())
    return ResponseModel("citizen with ID: {} name update is successful".format(id),
                         "citizen name updated successfully") \
        if updated_citizen \
        else ErrorResponseModel("An error occurred", 404, "There was an error updating the citizen.".format(id))

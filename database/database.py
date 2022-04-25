import motor.motor_asyncio
from bson import ObjectId
from decouple import config

from .database_helper import citizen_helper, admin_helper

MONGO_DETAILS = config('MONGO_DETAILS')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.citizens

citizen_collection = database.get_collection('citizens_collection')
admin_collection = database.get_collection('admins')

async def add_admin(admin_data: dict) -> dict:
    admin = await admin_collection.insert_one(admin_data)
    new_admin = await admin_collection.find_one({"_id": admin.inserted_id})
    return admin_helper(new_admin)

async def retrieve_citizens():
    citizens = []
    async for citizen in citizen_collection.find():
        citizens.append(citizen_helper(citizen))
    return citizens


async def add_citizen(citizen_data: dict) -> dict:
    citizen = await citizen_collection.insert_one(citizen_data)
    new_citizen = await citizen_collection.find_one({"_id": citizen.inserted_id})
    return citizen_helper(new_citizen)


async def retrieve_citizen(id: str) -> dict:
    citizen = await citizen_collection.find_one({"_id": ObjectId(id)})
    if citizen:
        return citizen_helper(citizen)


async def delete_citizen(id: str):
    citizen = await citizen_collection.find_one({"_id": ObjectId(id)})
    if citizen:
        await citizen_collection.delete_one({"_id": ObjectId(id)})
        return True


async def update_citizen_data(id: str, data: dict):
    citizen = await citizen_collection.find_one({"_id": ObjectId(id)})
    if citizen:
        citizen_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return True

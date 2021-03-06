from pydantic import BaseModel
from typing import Optional, List
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, HTTPException, Body
from main import imdb_collection
from db_collections.user import get_current_user

router = APIRouter(
    tags=["crud-routes"]
)

class Shows(BaseModel):
    show_id: str
    position: int
    title: str
    url: str
    type: str
    rating: float
    runtime: int
    year: int
    genres: List[str]
    votes: int
    date: str
    directors: List[str]

class UpdateShowModel(BaseModel):
    show_id: Optional[str]
    title: Optional[str]
    type: Optional[str]
    position: Optional[int]
    country: Optional[str]
    url: Optional[str]
    year: Optional[int]
    rating: Optional[int]
    runtime: Optional[int]
    votes: Optional[int]
    date: Optional[str]
    genres: Optional[str]

@router.get("/shows")
async def get_all_shows():
    #Use {_id: 0} to ignore the _id field when requesting: this is to prevent issues regarding ObjectIds in MongoDB
    shows = await imdb_collection.find({},{'_id': 0}).to_list(length=None)
    return shows

@router.post("/show", response_model = Shows)
async def create_show(show: Shows, user = Depends(get_current_user)):
    show = jsonable_encoder(show) #As this show is received as a JSON string, it must be decoded into a python dict first
    new_show = await imdb_collection.insert_one(show)
    created_show = await imdb_collection.find_one({"_id": new_show.inserted_id})
    return created_show
 
@router.delete("/{show_id}")
async def delete_show(show_id: str, user = Depends(get_current_user)):
    result = await imdb_collection.delete_one({"show_id": show_id})
    if result.deleted_count == 1: 
        return {"msg" : "Show has been successfully deleted!"}
    raise HTTPException(status_code = 404, detail="This show could not be deleted")

@router.put("/{show_id}")
async def update_show(show_id: str, show: UpdateShowModel = Body(...), user = Depends(get_current_user)):
    show = {k: v for k, v in show.dict().items() if v is not None} #Needed to remove missing fields
    if len(show) > 0: 
        updated_show = await imdb_collection.update_one({"show_id": show_id}, {"$set": show})
        return {"msg": "Show successfully updated!"}
    return {"msg": "Please input a updated show"}
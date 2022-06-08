from pydantic import BaseModel
from typing import Optional, List

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
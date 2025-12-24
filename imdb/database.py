from fastapi import APIRouter, HTTPException
from datetime import datetime
from typing import List
from schemas import User, UserCreate
from data import users_db, get_next_id

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[User])
async def get_users(sort_by: Optional[str] = None, order: Optional[str] = None,
                    name: Optional[str] = None, ):
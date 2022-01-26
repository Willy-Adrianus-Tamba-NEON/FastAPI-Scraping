from typing import Optional
from fastapi import APIRouter, Query
from apps.controllers import NewsController

router = APIRouter()

@router.get("/get_news")
async def get_news():
    data = NewsController.get_news_detail()
    return data


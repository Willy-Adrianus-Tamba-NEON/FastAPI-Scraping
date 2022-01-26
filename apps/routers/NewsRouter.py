import json
from typing import Optional
from unittest import result
from fastapi import APIRouter, Response, Body
from apps.controllers.NewsController import NewsController

router = APIRouter()

# Json dump input
add_news_example = json.dumps({
    "title": "",
    "link": "",
    "img_src": "",
    "author": "",
    "publisheddate": "",
    "content": "",
}, indent = 2)


# Endpoint
@router.get("/get_list_article")
async def get_list_article():
    result = get_list_article()
    return result

@router.get("/get_url_news_detail")
async def get_url_news_detail(response: Response, url:Optional[str]=None):
    result = NewsController.get_url_news_detail(url)
    response.status_code = result.status
    return result

@router.get("/get_news_detail")
async def get_news_detail(response: Response):
    result = NewsController.get_news_detail()
    response.status_code = result.status
    return result

@router.post("/save_news")
async def save_news(response: Response, input_data=Body(..., example=add_news_example)):
    result = NewsController.save_news(input_data=input_data)
    return result

@router.delete("/delete_news")
async def delete_news(response: Response, title:Optional[str]):
    result = NewsController.delete_news(title)
    return result


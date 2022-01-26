from datetime import date
from pydantic import BaseModel
from typing import Optional, List


class NewsData(BaseModel):
    title: str = None
    link: str = None
    img_src: str  = None
    author: str  = None
    publisheddate: date  = None
    content: str = None

class ListNews(BaseModel):
    title: str = None
    link: str = None

class ResponseNews(BaseModel):
    news_list: List[NewsData]

class ResponseListNews(BaseModel):
    url_list: List[ListNews]


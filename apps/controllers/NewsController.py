from apps.helper import Log
from apps.models import schema
from unittest import result
from apps.utils.News import get_news_detail, get_url_news_detail, get_list_article
from apps.schemas.Response import BaseResponse
from apps.schemas.NewsSchema import ResponseNews, ResponseListNews
from apps.models.NewsModel import News

class NewsController(object):
    @classmethod
    def get_list_article(cls):
        result = BaseResponse()
        result.status = 404

        try:
            data = get_list_article()
            result.status = 200
            result.message = "Success"
            result.data = data
            Log.info(result.message)

        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    def get_url_news_detail(cls, url = None):
        result = BaseResponse()
        result.status = 404

        try:
            if url is not None:
                data = get_url_news_detail(url)
                result.status = 200
                result.message = "Success"
                result.data = data
                Log.info(result.message)
            else:
                result.status = 400
                result.message = "Not a valid url"
                Log.info(result.message)

        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    def get_news_detail(cls):
        result = BaseResponse()
        result.status = 404
        # try:
        data = get_news_detail()
        result.status = 200
        result.message = "Success"
        result.data = data
        Log.info(result.message)

        # except Exception as e:
        #     Log.error(e)
        #     result.status = 400
        #     result.message = str(e)

        return result

    @classmethod
    def save_news(cls, input_data=None):
        result = BaseResponse()
        result.status = 400

        if not schema.has_table("kata_data"):
            with schema.create("kata_data") as table:
                table.string("title")
                table.string("link")
                table.string("img_src")
                table.string("author")
                table.string("publisheddate")
                table.string("content")

        try:
            if input_data is not None:
                News.insert(input_data)
                result.status = 200
                result.message = "Success"
                result.data = input_data
                Log.info(result.message)
            else:
                result.status = 400
                result.message = "No input data"

        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    def delete_news(cls, title=None):
        result = BaseResponse()
        result.status = 400

        try:
            if title is not None and title in News.lists("title"):
                News.where('title', title).delete()
                result.status = 200
                result.message = f"Success deleted news with title {title}"
            else:
                result.status = 400
                result.message = "Title not found"

        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result


from apps.helper import Log
from apps.models import schema, db
from unittest import result
from apps.utils.News import get_news_detail, get_news_detail_full, get_url_news_detail, get_list_article
from apps.schemas.Response import BaseResponse
from apps.schemas.NewsSchema import ResponseNews, ResponseListNews
from apps.models.NewsModel import News
from orator.exceptions.orm import ModelNotFound

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
        try:
            data = get_news_detail_full()
            result.status = 200
            result.message = "Success"
            result.data = data
            Log.info(result.message)

            # Cek apakah ada title yang sama di db. Jika tidak, insert scrape ke db
            try:
                for x in range(0, len(data)):
                    if data[x]['title'] not in News.lists("title"):
                        db.table('kata_data').insert(data[x])
                        Log.info("News doesn't exist - saved to db")
                    else:
                        Log.info("News exist - not saved to db")

            except Exception as e:
                Log.info(e)
            

        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

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
                table.text("content")

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


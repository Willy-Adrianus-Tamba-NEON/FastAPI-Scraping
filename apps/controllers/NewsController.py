from pkgutil import get_data
from apps.utils.News import get_news_detail

class NewsController(object):
    @classmethod
    def get_news_detail():
        data = get_news_detail
        return data


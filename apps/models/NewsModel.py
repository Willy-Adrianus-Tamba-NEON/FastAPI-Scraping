from apps.models import Model


class News(Model):
    __table__ = 'kata_data'
    __primary_key__ = 'title'
    __timestamps__ = False

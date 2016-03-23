from django.conf.urls import url

from maps import api

urlpatterns = [
    url(r'^store_point$', api.store_point, name='api_store_point'),
]
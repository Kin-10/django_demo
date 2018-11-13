from django.conf.urls import url
from . import views_home

urlpatterns = [
    url(r'^$',views_home.page_index),
    url(r'^data/',views_home.page_data),
]

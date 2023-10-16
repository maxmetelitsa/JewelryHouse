from django.contrib import admin
from django.urls import path
from JewelryHouseWebsite.views import (index_page, jewelryMarket_page, news_page,
stockists_page, about_page)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('index.html'.lower(), index_page),
    path('jewelryMarket.html'.lower(), jewelryMarket_page),
    path('news.html'.lower(), news_page),
    path('stockists.html'.lower(), stockists_page),
    path('about.html'.lower(), about_page)
]

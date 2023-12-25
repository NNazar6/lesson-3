from django.contrib import admin
from django.urls import path, re_path, include
from app import views

product_patterns = [
    path('pp', views.pop_post),
    path('lp', views.last_post),
    path('ps', views.posts),
]


for_post = [
    path('like', views.likes),
    path('comm', views.comm),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('posts/<int:id>/', include(for_post)),
    path('posts1/', include(product_patterns)),
    path('about', views.about),
    path('contacts', views.contacts),
    path('err', views.err),
    path('adm', views.access),
    path('json', views.json),
    path('set', views.set),
    path('get', views.get),
]

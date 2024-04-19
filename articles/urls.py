from django.urls import path
from django import forms
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "articles"
urlpatterns = [
    path("mainpage/", views.mainpage, name="mainpage"),
    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/edit", views.edit, name="edit"),
    path("<int:pk>/update/", views.update, name="update"),
    path("sorted_articles/", views.sorted_articles, name="sorted_articles"),


    path("<int:pk>/like/", views.like, name="like"),
    
    
    path("<int:pk>/comments/", views.comment_create, name="comment_create"),
    
    path("<int:pk>/comments/<int:comment_pk>/delete/",views.comment_delete,name="comment_delete"),
    path('search/', views.search_articles, name='search'),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

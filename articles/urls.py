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

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
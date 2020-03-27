from django.urls import path
from . import views

urlpatterns = [
    path("404/", views.page_not_found),
    path("500/", views.server_error),
    path("", views.Index.as_view(), name="index"),
    path("upload/", views.Upload.as_view(), name="upload"),
    path("search/", views.Search.as_view(), name="search"),
    ]

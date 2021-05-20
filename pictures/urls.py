from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from pictures.views import (
    PictureListView,
    PicureDetailView,
    PictureFeaturedView,
    PictureCategoryView,
)

pictures_list = PictureListView.as_view({"post": "create", "get": "list"})
pictures_detail = PicureDetailView.as_view({"get": "retrieve", "put": "update", "delete":"destroy"})

urlpatterns = format_suffix_patterns(
    [
        path("", pictures_list, name="pictures_list"),
        path("featured", PictureFeaturedView.as_view()),
        path("category", PictureCategoryView.as_view()),
        path("<slug>", pictures_detail, name="pictures_detail"),
    ]
)

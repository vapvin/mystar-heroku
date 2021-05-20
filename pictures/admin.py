from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import PictureModel


class PictureAdminModel(SummernoteModelAdmin):
    exclude = ("slug",)
    list_display = ("id", "title", "category", "price", "date_created")
    list_display_links = ("id", "title")
    search_fields = ("title",)
    summernote_fields = ("description",)


admin.site.register(PictureModel, PictureAdminModel)
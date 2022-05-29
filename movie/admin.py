from django.contrib import admin
from .models import *



@admin.register(Genre)
class GenresAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    list_display_links = ["name"]
    prepopulated_fields = {"slug": ("name",)}



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author","city","slug"]
    list_display_links = ["title"]
    prepopulated_fields = {"slug":("title",)}
from django.contrib import admin
from .models import Book

# Register your models here.
# admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'price', 'is_published','published', 'cover_image']
    list_display = ['title', 'price']
    list_filter = ['published']
    search_fields = ['title', 'description']


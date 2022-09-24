from django.contrib import admin
from APP_LEARNING.models import Book

#admin.site.register(Book)
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','price','cover_tag']
    search_fields = ['title','descrption']
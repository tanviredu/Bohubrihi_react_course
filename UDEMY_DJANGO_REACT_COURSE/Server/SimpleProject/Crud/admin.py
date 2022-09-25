from django.contrib import admin
from .models import Book,BookNumber,Character,Author

admin.site.register(Book)
admin.site.register(BookNumber)
admin.site.register(Character)
admin.site.register(Author)

# Register your models here.

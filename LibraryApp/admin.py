from django.contrib import admin
from .models import Author, Book, List

# Register your models here.

class BookAdmin(admin.ModelAdmin):

    list_display = ("title", "genre", "year", "pages")
    search_fields = ("title",)
    list_filter = ("title", "genre", "year", "pages")
    prepopulated_fields = {'slug': ('title',)}
    
class ListAdmin(admin.ModelAdmin):
    
    list_display = ("name", "created", "modified")
    search_fields = ("name",)
    list_filter = ("name", "created", "modified")

admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(List, ListAdmin)
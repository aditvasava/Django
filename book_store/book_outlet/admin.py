from django.contrib import admin
from .models import Book, Author, Address

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug", )
    prepopulated_fields = {"slug": ("title",)}

    # displays a filter that can be done on author and rating
    list_filter = ("author", "rating")

    # displays title & author data as individual columns
    list_display = ("title", "author")

# After writing below line, we can see the appname and the Book model from the admin UI
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
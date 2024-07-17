from django.contrib import admin
from .models import Book, Author, Address
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug", )
    prepopulated_fields = {"slug": ("title", )}
    list_filter = ("rating", "title")
    list_display = ("id", "title", "rating", "author")

class AuthorAdmin(admin.ModelAdmin):

    list_display = ("first_name", "last_name", )
    list_filter = ("first_name", )

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address)

# Need to create a second model and check whether it is working or not.
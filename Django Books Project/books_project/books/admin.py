from django.contrib import admin
from .models import Book, Author, Address, Country
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug", )
    prepopulated_fields = {"slug": ("title", )}
    list_filter = ("rating", "title")
    list_display = ("id", "title", "rating", "author", "country_published")

class AuthorAdmin(admin.ModelAdmin):

    list_display = ("first_name", "last_name", )
    list_filter = ("first_name", )

class AddressAdmin(admin.ModelAdmin):

    list_filter = ('city', 'pincode')


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country)

# Need to create a second model and check whether it is working or not.
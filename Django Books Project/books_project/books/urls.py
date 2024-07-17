from django.urls import path, include
from books import views

urlpatterns = [
    path("test", views.all_books),
    path("add_book/", views.add_book),
    path("delete_book/<int:id>", views.delete_book), 
    path("detail_book/<str:slug>", views.detail_book,name = "model_detail")
]

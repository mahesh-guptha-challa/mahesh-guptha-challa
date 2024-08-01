from . import views
from django.urls import path

urlpatterns = [
    path("author/<int:id>", views.author, name='authorlink'),
    path("tag/<int:id>", views.tag, name='tag'),
    path("post/<slug:slug>", views.post, name = "post"),
    path("", views.all_posts)
]

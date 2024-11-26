from . import views
from django.urls import path

urlpatterns = [
    # path("author/<int:id>", views.author, name='authorlink'),
    path("author/<int:pk>", views.AuthorView.as_view(), name='authorlink'),
    # path("tag/<int:id>", views.tag, name='tag'),
    path("tag/<int:pk>", views.TagClass.as_view(), name='tag'),
    # path("post/<slug:slug>", views.post, name = "post"),
    path("post/<slug:slug>", views.UpdatePost.as_view(), name = "post"),
    # path("", views.all_posts),
    path("", views.AllPostView.as_view(), name="AllPosts"),
    # path("post/<slug:slug>/comments", views.comments, name = "submit_form"),
    # path("post/<slug:slug>/comments", views.CommentsView.as_view(), name = "submit_form"),
    # path("post/read_later/save", views.read_later, name="read_later"),
    path("post/read_later/save", views.ReadLaterView.as_view(), name="read_later")
]

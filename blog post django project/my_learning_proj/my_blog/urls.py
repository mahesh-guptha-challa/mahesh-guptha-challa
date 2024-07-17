from django.urls import path
# from my_blog import views
from . import views


urlpatterns = [
    path("", view=views.main, name="welcomepage"),
    path("allposts", view=views.all_posts, name="allblogs"),
    path("singlepost/<str:post_name>", views.single_post, name="eachpost")]

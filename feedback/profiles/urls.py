from django.urls import path
from profiles import views

urlpatterns = [
    path("", views.CreateProfileView.as_view(), name =  "image"),
    path("list", views.viewsListProfileView.as_view())
]

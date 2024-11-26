from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.FeedbackView.as_view(), name = "feedback"),
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.ReviewView.as_view()),
    path("review/<int:pk>", views.ReviewEachView.as_view(), name="data"),
    path("reviews/favourite", views.FavouriteView.as_view())
    ]
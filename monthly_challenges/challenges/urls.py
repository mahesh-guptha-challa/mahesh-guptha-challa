from . import views
from django.urls import path

urlpatterns = [path("<int:month>", views.challenges_by_number),
path("<str:month>", views.challenges_direct, name="str-month"),
path("", view=views.challenges_list, name="all_challenges")]
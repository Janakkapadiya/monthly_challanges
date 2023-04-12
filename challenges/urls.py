from . import views
from django.urls import path


urlpatterns = [
    path("", views.list_of_months),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month_challange")
]

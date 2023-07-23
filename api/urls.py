from django.urls import path
from api.views import hello, ProfileListCreateView

urlpatterns = [
    path("", hello),
    path("profile", ProfileListCreateView.as_view()),
]

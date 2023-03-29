from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home-page"),
    path('about-us', views.AboutView.as_view(), name="about-page"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactUsView.as_view(), name="contact-us"),
    path('profile/', views.CreateProfileView.as_view(), name="create-profile-page"),
]
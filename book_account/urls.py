from django.urls import path
from . import views

urlpatterns = [
    path('register', views.RegisterView.as_view(), name="register-page"),
    path('login', views.LoginView.as_view(), name="login-page"),
    path('forget-password', views.ForgetPassword.as_view(), name="forget-password-page"),
    path('activate-account/<email_active_code>', views.ActivateAccount.as_view(), name="activate-account")
]

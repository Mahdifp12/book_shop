from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserPanelDashboardPage.as_view(), name="user_panel_page"),
    path('edit-profile', views.EditUserProfilePage.as_view(), name="edit_user_profie"),
]

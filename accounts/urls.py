from django.urls import path
from django.contrib.auth import views as auth_views
from .import views




app_name= 'accounts'



urlpatterns = [
    path("register", views.registration_view, name='register'),
    path("account-info", views.AccountView.as_view(), name="info"),
    # path("login/", views.my_login, name='login'),
    # path("logout/", views.logout_view, name='logout'),
]
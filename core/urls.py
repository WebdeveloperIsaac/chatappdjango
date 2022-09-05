from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontend,name="frontpage"),
    path('signup/',views.signup,name="Signup"),
    path('logout/',auth_views.LogoutView.as_view(),name="logout"),
    path('login/',auth_views.LoginView.as_view(template_name="core/login.html"),name="login")
]
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import RegisterUser, Login

urlpatterns = [
    path("", views.base, name="base"),
    path('account/', views.profile_view, name="account"),
    path('auth/', Login.as_view(), name="auth"),
    path("logout/", LogoutView.as_view()),
    path('register/', RegisterUser.as_view(), name="register"),
    path("service/", views.Service, name="service"),
    path("service/index.html",views.base, name="")
]

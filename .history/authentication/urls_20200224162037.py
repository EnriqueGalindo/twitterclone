from django.contrib import admin
from django.urls import path
from .views import (
    Login,
    Logout,
    Register,
)


urlpatterns = [
    path('login/', login_view)
    path('logout/', Logout)
]
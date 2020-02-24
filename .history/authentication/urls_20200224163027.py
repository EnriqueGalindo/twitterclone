from django.contrib import admin
from django.urls import path
from .views import (
    login_view,
    logout,
    register,
)


urlpatterns = [
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view)
]
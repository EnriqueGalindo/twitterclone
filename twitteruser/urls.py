from django.urls import path
from .views import (
    login_view,
    logout_view,
    Register,
    # following_view,
    user_view,
    FollowingView
)


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view,),
    path('register/', Register.as_view()),
    path('follow/<int:id>/', FollowingView.as_view()),
    path('user/<int:id>/', user_view)
]

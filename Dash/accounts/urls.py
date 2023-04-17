from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('', views.SignInView.as_view(), name='user_signin'),
    path('signup/', views.SignUpView.as_view(), name='user_signup'),
    path('signout/', views.SignOutView.as_view(), name='user_signout'),
]
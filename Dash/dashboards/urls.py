from django.urls import path
from . import views


app_name = 'dashboards'
urlpatterns = [
    path('userPanel/', views.DashboardView.as_view(), name='user_panel'),
    path('edit/', views.CreateView.as_view(), name='user_info'),
    path('ticket/', views.TicketView.as_view(), name='user_ticket')
]

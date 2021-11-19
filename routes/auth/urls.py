from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view),
    path('register/', views.register),
    path('verify_email/<str:verification_token>/', views.verify_email),
    path('password_reset/', views.password_reset),
    path('password_reset/confirm/<str:reset_token>/', views.password_reset_confirm)
]

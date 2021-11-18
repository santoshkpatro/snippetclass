from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view),
    path('register/', views.register),
    path('verify_email/<str:verification_token>/', views.verify_email)
]

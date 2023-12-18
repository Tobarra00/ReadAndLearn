from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Authenticate.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('logout/', views.close_session, name='logout'),
]
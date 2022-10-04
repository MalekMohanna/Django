from django.urls import path 
from .import views


app_name='FirstApp'
urlpatterns = [
    path("", views.index),
    path("create_user", views.create_user),
    path("success", views.success),
    path("logout", views.logout),
    path("login",views.proc_login)
]
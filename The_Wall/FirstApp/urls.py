from django.urls import path 
from .import views

urlpatterns = [
    path("", views.index),
    path("create_user", views.create_user),
    path("wall", views.success),
    path("create_post",views.create_post),
    path("create_comment",views.create_comment),
    path("logout", views.logout),
    path("login",views.proc_login),
    path('<int:message_id>/delete', views.deleteMessage),
]
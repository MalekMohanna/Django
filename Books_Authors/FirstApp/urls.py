from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('add',views.add),
    path('authors/',views.authors),
    path('books/<int:book_id>',views.books),
    path('authors/<int:author_id>',views.showAu),
    ]
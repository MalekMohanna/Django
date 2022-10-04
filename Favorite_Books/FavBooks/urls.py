from django.urls import path

import FirstApp
from .import views
app_name='FavBooks'
urlpatterns = [
    path("books", views.root),
    path('books/create',views.create_book),
    path('books/<int:id>',views.the_book),
    path('books/<int:id>/unfavorite', views.books_unfavorite),
    path('books/<int:id>/favorite', views.books_addFavorite),
    path('books/<int:id>/update', views.books_update),
    path('books/<int:id>/delete', views.books_delete),
    path('books/<int:id>/delete', views.books_delete),
    path('user/logout', views.logout_user),
]
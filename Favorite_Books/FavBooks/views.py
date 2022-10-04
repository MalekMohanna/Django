from django.contrib import messages
from multiprocessing import context
from django.shortcuts import render,redirect
from FirstApp.models import User
from .models import Book


# Create your views here.

def root(request):
    context = {
        "new_user" : User.objects.get(id=request.session["user_id"]),
        "all_books": Book.objects.all(),
    }
    return render(request,'books.html',context)

def create_book(request):
    if request.method == "POST":
        errors=Book.objects.book_validation(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/books')
        the_user = User.objects.get(id=request.session["user_id"])
        book = Book.objects.create(title = request.POST['title'],description = request.POST['description'] , uploadedby = the_user, )
        the_user.liked_books.add(book)
        return redirect(f'/books/{book.id}')
    return redirect('/')

def the_book(request,id):
    context = {
        "new_user" : User.objects.get(id=request.session["user_id"]),
        "all_books": Book.objects.get(id=id),
    }
    return render(request,'booksid.html',context)

def books_unfavorite(request, id):
    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=id)
    user.liked_books.remove(book)
    return redirect(f'/books/{id}')

def books_addFavorite(request, id):
    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=id)
    user.liked_books.add(book)
    return redirect(f'/books/{id}')

def books_update(request, id):
    errors = Book.objects.update_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/books/{id}')
    book = Book.objects.get(id=id)
    book.title = request.POST['title']
    book.description = request.POST['description']
    book.save()
    return redirect('/books')

def books_delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('/books')

def logout_user(request):
    request.session.clear()
    return redirect('/')
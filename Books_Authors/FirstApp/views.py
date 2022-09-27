from multiprocessing import context
from turtle import title
from django.shortcuts import render,redirect
from .models import Book,Author
def index(request):
    context={
        'my_book':Book.objects.all(),
        'my_author':Author.objects.all(),
    }
    return render(request,'index.html',context)

def authors(request):
    context={
        'my_book':Book.objects.all(),
        'my_author':Author.objects.all(),
    }
    return render(request,'authors.html',context)

def books(request,book_id):
    context={
        'my_book':Book.objects.get(id=book_id),
        'the_authors':Author.objects.all(),
    }
    return render(request,'books.html',context)

def showAu(request,author_id):
    context={
        'my_book':Book.objects.all(),
        'the_authors':Author.objects.get(id=author_id),
    }
    return render(request,'showAu.html',context)

def add(request):
    if request.POST['book-or-author']=='book':
        x= Book.objects.create(title=request.POST['title'],desc=request.POST['desc'])
        x.save()
        return redirect('/')
    elif request.POST['book-or-author']=='author':
        x=Author.objects.create(first_name= request.POST['f-name'],last_name= request.POST['l-name'],notes= request.POST['notes'])
        x.save()
        return redirect('authors/')
    elif request.POST['book-or-author']=='assign-a':
        a=Author.objects.get(id=request.POST['sel-auth'])
        b=Book.objects.get(id=request.POST['book-id'])
        b.authors.add(a)
        return redirect('/')
    elif request.POST['book-or-author']=='assign-b':
        a=Author.objects.get(id=request.POST['author-id'])
        b=Book.objects.get(id=request.POST['sel-book'])
        b.authors.add(a)
        return redirect('/authors')

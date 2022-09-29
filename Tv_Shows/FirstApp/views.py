from multiprocessing import context
from django.shortcuts import render,redirect
from .models import Show

def index(request):
    return redirect('/shows')

def root(request):
    context={
        'my_shows': Show.objects.all()
    }
    return render(request,'index.html',context)

def new(request):
    return render(request,'new.html')

def create(request):
    x = Show.objects.create(title=request.POST['show-t'],network=request.POST['netw'],release_date=request.POST['release-d'],descreption=request.POST['descr'])
    x.save()
    id=str(Show.objects.last().id)
    return redirect('/shows/'+id)

def shows(request,id):
    z=id
    context={
        'created_show':Show.objects.get(id=z)
    }
    return render(request,'show.html',context)

def edit(request,id):
    context={
        'my_id':str(id),
        'my_show':Show.objects.get(id=id),
        'show_release':Show.objects.get(id=id).release_date.strftime('%Y-%m-%d')
    }
    return render(request,'edit.html',context)

def update(request,id):
    print('hiiii')
    my_id=id
    to_update=Show.objects.get(id=my_id)
    to_update.title=request.POST['show-t']
    to_update.network=request.POST['netw']
    to_update.release_date=request.POST['release-d']
    to_update.descreption=request.POST['descr']
    to_update.save()
    return redirect('/shows/'+id)

def delete(request,id):
    x=Show.objects.get(id=id)
    x.delete()
    return redirect('/shows')
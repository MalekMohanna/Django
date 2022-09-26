from multiprocessing import context
from venv import create
from django.shortcuts import render,redirect
from .models import Dojo,Ninja

def index(request):
    context = {
        'my_dojo':Dojo.objects.all(),
    }
    return render(request,'index.html',context)

def entry(request):
    if request.POST['dojo-ninja'] == 'dojo':
        x = Dojo.objects.create(name = request.POST['f-named'],city = request.POST['city'],state = request.POST['state'])
        x.save()
    else:
        y = Ninja.objects.create(dojo = Dojo.objects.get(name=request.POST['dojo']),first_name = request.POST['f-namen'],last_name = request.POST['l-name'])
        y.save()
    return redirect('/')

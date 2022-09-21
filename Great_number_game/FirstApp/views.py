from ast import Num
from multiprocessing import context
from django.shortcuts import render,redirect
from random import randint, random

def root(request):
        return render(request,'index.html')



def check(request):
    rand_numx=randint(1,100)
    if 'my_rand' not in request.session :
        request.session['my_rand'] = rand_numx
    print(request.session['my_rand'])
    my_guess=int(request.POST['guess'])
    context = {
        'winner':my_guess
    }
    print(my_guess)
    if my_guess == request.session['my_rand']:
        del request.session['my_rand']
        return render(request,'correct.html',context=context)
    elif my_guess > request.session['my_rand']:
        return render(request,'toohigh.html')
    elif my_guess < request.session['my_rand']:
        return render(request,'toolow.html')

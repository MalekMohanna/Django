from ast import Pass
from multiprocessing import context
from django.shortcuts import render,redirect
from random import randint
from datetime import datetime

def index(request):
    if 'total_gold' not in request.session :
        request.session['total_gold']=0
        request.session['log']=[]
    return render(request,'index.html')

def generate(request):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    if request.POST['where'] != 'quest' :
        place = request.POST['where']
        gold=randint(10,20)
        sucess=randint(1,2)
    elif request.POST['where'] == 'quest':
        place = request.POST['where']
        gold=randint(0,50)
        sucess=randint(1,2)
    if sucess == 2 :
        gold = gold * -1
        request.session['log'].append(f"You have failed a quest and lost {gold} gold. Ouch ( {now} ) ")
    elif sucess == 1 :
        request.session['log'].append(f"You have entered a {place} and earned {gold} gold. ( {now} ) ")
    request.session['total_gold']+=gold
    return redirect('/')

def clear(request):
    del request.session['total_gold']
    del request.session['log']
    return redirect('/')
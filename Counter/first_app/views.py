from multiprocessing import context
from django.shortcuts import render, HttpResponse
def root(request):
    # print(request.session['num_visits'])
    num_visits = request.session['num_visits']
    request.session['num_visits'] = num_visits + 1
    num_visits = request.session['num_visits']
    context = {
        'visits_num': num_visits,
    }
    return render(request,"index.html",context=context)

def destroy(request):
    request.session['num_visits']=0
    num_visits = request.session['num_visits']
    context = {
        'visits_num':num_visits
    }
    return render(request,'index.html',context=context)
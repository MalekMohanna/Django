from multiprocessing import context
from django.shortcuts import render, HttpResponse,redirect
def root(request):
    return render(request, "index.html")

def create_user(request):
    name_from_form=request.POST['name']
    location_from_form=request.POST['location']
    language_from_form=request.POST['Language']
    comment_from_form=request.POST['comment']
    OS_from_form=request.POST['OS']
    answer_from_form=request.POST['answer']
    context={
        'user_name':name_from_form,
        'user_location':location_from_form,
        'user_language':language_from_form,
        'user_comment':comment_from_form,
        "user_os":OS_from_form,
        'user_answer':answer_from_form,
    }
    print(request.POST)
    return render(request,'result.html',context)

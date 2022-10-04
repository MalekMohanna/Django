import bcrypt
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User,Message,Comment

# Create views here!
def index(request):
    return render(request, "index.html")

def create_user(request):
    errors = User.objects.new_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect("/")

    else:
        newFirstName = request.POST["first_name"]
        newLastName = request.POST["last_name"]
        newEmail = request.POST["email"]
        password = request.POST["password"]
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(first_name=newFirstName, last_name=newLastName, email=newEmail, password=pw_hash)
        request.session["user_id"] = new_user.id
        return redirect("/wall")

def success(request):
    if "user_id" not in request.session:
        return redirect("/")
    context = {
        "all_messages": Message.objects.all(),
        "user" : User.objects.get(id=request.session["user_id"]),
        'comments' : Comment.objects.all(),
    }
    return render(request, "success.html", context)

def proc_login(request):
    if request.method != "POST":
        return redirect("/")
    valid = User.objects.login_validator(request.POST)
    if len (valid["errors"]) > 0:
        for key, value in valid["errors"].items():
            messages.error(request,value)
        return redirect("/")
    else:
        request.session["user_id"] = valid["user"].id
        return redirect ("/wall")
    
    


def create_post(request):
    x= Message.objects.create(message=request.POST['content'],poster=User.objects.get(id=request.session["user_id"]))
    return redirect('/wall')

def create_comment(request):
    x= Comment.objects.create(comment=request.POST['content'],poster=User.objects.get(id=request.session["user_id"]),message=Message.objects.get(id=request.POST['message']))
    return redirect('/wall')

def deleteMessage(request, message_id):
    delete = Message.objects.get(id=message_id)
    delete.delete()
    return redirect('/wall')

def logout(request):
    request.session.clear()
    return redirect ("/")
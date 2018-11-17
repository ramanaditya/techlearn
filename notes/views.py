from django.shortcuts import render
from django.utils import timezone
from notes.forms import UserForm,notes_form
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from .models import notes
from .forms import CommentForm

def index(request):
    return render(request, 'notes/index.html')

# def file_python(request):
#     note_python = notes.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'notes/file_python.html',{'note_python':note_python})

def django_notes(request):
    django_list = []
    note = notes.objects.order_by('tag')

    for entry in note:
        if entry.tag == 'DJANGO':
            django_list.append(entry)
    return render(request, 'notes/notes.html',{'django_list':django_list,})

def c_notes(request):
    c_list = []
    note = notes.objects.order_by('tag')

    for entry in note:
        if entry.tag == 'C/C++':
            c_list.append(entry)
    return render(request, 'notes/notes.html',{'c_list':c_list,})

def java_notes(request):
    java_list = []
    note = notes.objects.order_by('tag')

    for entry in note:
        if entry.tag == 'JAVA':
            java_list.append(entry)
    return render(request, 'notes/notes.html',{'java_list':java_list,})

def mysql_notes(request):
    mysql_list = []
    note = notes.objects.order_by('tag')

    for entry in note:
        if entry.tag == 'MYSQL':
            mysql_list.append(entry)
    return render(request, 'notes/notes.html',{'mysql_list':mysql_list,})

def javascript_notes(request):
    javascript_list = []
    note = notes.objects.order_by('tag')

    for entry in note:
        if entry.tag == 'JAVASCRIPT':
            javascript_list.append(entry)
    return render(request, 'notes/notes.html',{'javascript_list':javascript_list,})

def machine_learning_notes(request):
    machine_learning_list = []
    note = notes.objects.order_by('tag')

    for entry in note:
        if entry.tag == 'MACHINE_LEARNING':
            machine_learning_list.append(entry)
    return render(request, 'notes/notes.html',{'machine_learning_list':machine_learning_list,})

def front_end_notes(request):
    front_end_list = []
    note = notes.objects.order_by('tag')

    for entry in note:
        if entry.tag == 'FRONT_END':
            front_end_list.append(entry)
    return render(request, 'notes/notes.html',{'front_end_list':front_end_list,})


def python_notes(request):
    python_list = []


    note = notes.objects.order_by('tag')

    for entry in note:
        if entry.tag == 'PYTHON':
            python_list.append(entry)

    return render(request, 'notes/notes.html',{'python_list':python_list,})

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = User.objects.create_user(username=request.POST['username'],
                                            email=request.POST['email'],
                                            password=request.POST['password'])
            # user.save()
            # user.set_password(user.password)

            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'notes/registration.html',{'user_form':user_form,
                                                     'registered':registered})

def user_login(request):
    print(request, request.method)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                print("login successful")
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("account not active")
        else:
            print("login failed for {}".format(username))
            return HttpResponse("invalid login credentials !!")
    return render(request, 'notes/login.html')
from django.contrib.auth.views import LoginView, LogoutView


# class UserLoginView(LoginView):
#     template_name = 'notes/login.html'



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('logout'))





@login_required

def add(request):
    posted = False
    if request.method == 'POST':
        user_form =notes_form(request.POST)

        if user_form.is_valid():
            username = user_form.cleaned_data.get('content')
            #raw_password = user_form.cleaned_data.get('post_comment')
            user_form.save()

            posted = True
        else:
            print(user_form.errors)
    else:
        user_form = notes_form()
    return render(request,'notes/addtocomment.html',{'user_form':user_form,
                                                     'posted':posted})



def comment(request):
    posted=False

    if request.method == 'POST':
        user_form =CommentForm(request.POST)
        python_comment = []
        if user_form.is_valid():
            username = user_form.cleaned_data.get('name')
            raw_password = user_form.cleaned_data.get('post_comment')
            user_form.save()
            posted=True
            com = comments.objects.all()


            python_comment.append(com)
            return render_to_response('notes/notes.html',{'python_comment':python_comment,})
        else:
            print(user_form.errors)
    else:
        user_form = CommentForm()
    return render(request,'notes/comment.html',{'user_form':user_form,'posted':posted},)

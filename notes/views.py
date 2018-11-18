from django.shortcuts import render
from django.utils import timezone
from notes.forms import UserForm,notes_form,CommentForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from .models import notes,comments
from .forms import CommentForm

def index(request):
    return render(request, 'notes/index.html')

# def file_python(request):
#     note_python = notes.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'notes/file_python.html',{'note_python':note_python})

def django_notes(request):
    django_list = []
    django_comment=[]
    note = notes.objects.order_by('tag')
    comment = comments.objects.order_by('comment_tag')
    for entry in note:
        if entry.tag == 'DJANGO':
            django_list.append(entry)
    for entry in comment:
        if entry.comment_tag == 'DJANGO':
            django_comment.append(entry)
    return render(request, 'notes/notes.html',{'django_list':django_list,'django_comment':django_comment,})

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
    python_comment=[]

    note = notes.objects.order_by('tag')
    comment = comments.objects.order_by('comment_tag')
    for entry in note:
        if entry.tag == 'PYTHON':
            python_list.append(entry)
    for entry in comment:
        if entry.comment_tag == 'PYTHON':
            python_comment.append(entry)
    return render(request, 'notes/notes.html',{'python_list':python_list,'python_comment':python_comment,})

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
    return render(request, 'notes/login.html',{'user':user,})
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
            tag_name = user_form.cleaned_data.get('tag')
            note = notes.objects.order_by('tag')
            #raw_password = user_form.cleaned_data.get('post_comment')
            user_form.save()

            posted = True

            #a = ['PYTHON','DJANGO','JAVA','MYSQL','MACHINE_LEARNING','JAVASCRIPT','FRONT_END','C/C++']
            #tag_list = []
            #for entry in note:
            if tag_name == 'PYTHON':
                return python_notes(request)
                #tag_list.append('python_list')
            elif tag_name == 'DJANGO':
                return django_notes(request)
            elif tag_name == 'JAVA':
                return java_notes(request)
            elif tag_name == 'MYSQL':
                return java_notes(request)
            elif tag_name == 'MACHINE_LEARNING':
                return machine_learning_notes(request)
            elif tag_name == 'JAVASCRIPT':
                return javascript_notes(request)
            elif tag_name == 'FRONT_END':
                return front_end_notes(request)
            else:
                return c_notes(request)
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
        
        if user_form.is_valid():
            name = user_form.cleaned_data.get('name')
            comment_tag = user_form.cleaned_data.get('comment_tag')
            post_comment = user_form.cleaned_data.get('post_comment')
            user_form.save()
            posted=True
            if comment_tag == 'PYTHON':
                return python_notes(request)
                #tag_list.append('python_list')
            elif comment_tag == 'DJANGO':
                return django_notes(request)
            elif comment_tag == 'JAVA':
                return java_notes(request)
            elif comment_tag == 'MYSQL':
                return java_notes(request)
            elif comment_tag == 'MACHINE_LEARNING':
                return machine_learning_notes(request)
            elif comment_tag == 'JAVASCRIPT':
                return javascript_notes(request)
            elif comment_tag == 'FRONT_END':
                return front_end_notes(request)
            else:
                return c_notes(request)
            #return render_to_response('notes/notes.html',{'python_comment':python_comment,})
        else:
            print(user_form.errors)
    else:
        user_form = CommentForm()
    return render(request,'notes/comment.html',{'user_form':user_form,'posted':posted},)

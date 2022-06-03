from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from .models import Post
from django.http import  HttpResponseRedirect
from django.contrib import messages
# Create your views here.


def home1(request):
    return render(request, 'main/home1.html')
    posts = Post.objects.all()
    return render(request, 'main/home1.html', {'posts': posts})



@login_required(login_url='/login/')
def create_post(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            post.author = request.user
            post.save()
        else:
            form=PostForm()   
        return render(request, 'main/create_post.html',{'form':form})    

@login_required(login_url='/login')
def sign_up(request):
    if rquest.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm() 

    return render(request, 'registration/sign_up.html', {'form': form})    

@login_required(login_url="/login")
def home(request):
    posts = Post.objects.all()

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        user_id = request.POST.get("user-id")

        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and (post.author == request.user or request.user.has_perm("main.delete_post")):
                post.delete()
        elif user_id:
            user = User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.get(name='default')
                    group.user_set.remove(user)
                except:
                    pass

                try:
                    group = Group.objects.get(name='mod')
                    group.user_set.remove(user)
                except:
                    pass

    return render(request, 'main/home.html', {"posts": posts})


def post_detail(request, pk):
    post = Post.objects.filter(id=pk).first()
    return render(request, 'main/post_detail.html', {"post": post})


def post_update(request, pk):
    post = Post.objects.filter(id=pk).first()
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = PostForm(instance=post)
    return render(request, 'main/post_update.html', {"form": form})


def delete_post(request, pk):
    post = Post.objects.filter(id=pk).first()
    if post and (post.author == request.user or request.user.has_perm("main.delete_post")):
        post.delete()
    return redirect('/home')


@login_required(login_url="registration/login")
@permission_required("main.add_post", login_url="registration/login", raise_exception=True)
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/home")
    else:
        form = PostForm()

    return render(request, 'main/create_post.html', {"form": form})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})

def Individual(request):
    return render(request, 'bookings/individual.html')

def home(request):
    return render(request, 'main/home.html')

def home1(request):
    return render(request, 'main/home1.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')


def booking(request):
    return render(request, 'bookings/booking.html')


def group(request):
    return render(request, 'bookings/group.html')


def turriding(request):
    return render(request, 'bookings/turriding.html')





def member(request):
    return render(request, 'main/member.html')


def horses(request):
    return render(request, 'main/horses.html')


def gallery(request):
    return render(request, 'main/gallery.html')


def ridschool(request):
    return render(request, 'main/ridschool.html')


def calendar(request):
    return render(request, 'main/calendar.html')


def footer(request):
    return render(request, 'main/footer.html')


def nav(request):
    return render(request, 'main/nav.html')

def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out!"))
    return redirect('home')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request,"There Was An Error Logging In, Try Again...")
            return redirect('login')


    else:
        return render(request, 'registration/login.html', {})


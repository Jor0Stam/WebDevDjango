from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from .models import BlogPost, Tag, Comment
from .forms import BlogPostCreateModelForm, TagCreateModelForm, CommentForm, LoginForm, RegisterForm
from .decorators import anonymous_required

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url=reverse_lazy('login'))
def index(request):
    if request.session:
        return register_view(request)

    blogs = BlogPost.objects.all()
    return render(request, 'index.html', locals())

@login_required(login_url=reverse_lazy('login'))
def detail_blog(request, title):
    bl = BlogPost.objects.filter(title=title).first()
    comment_form = CommentForm()

    # import ipdb; ipdb.set_trace()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = Comment(email=comment_form.cleaned_data.get('email'),
                              content=comment_form.cleaned_data.get('content'))
            comment.save()

            bl.comments.add(comment)
            bl.save()


    return render(request, 'detail-blog.html', locals())

@login_required(login_url=reverse_lazy('login'))
def create_blog(request):
    form = BlogPostCreateModelForm()

    if request.method == 'POST':
        form = BlogPostCreateModelForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('blog:index'))

    return render(request, 'create-blog.html', locals())

@login_required(login_url=reverse_lazy('login'))
def create_tag(request):
    form = TagCreateModelForm()
    if request.method == 'POST':
        form = TagCreateModelForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('blog:index'))

    return render(request, 'create-tag.html', locals())

@anonymous_required(login_url=reverse_lazy('logout'))
def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
           user = authenticate(**form.cleaned_data)
           if user is None:
               form.add_error(field='', error='No such User')
           else:
               login(request, user)

    return render(request, 'login.html', locals())

@anonymous_required(login_url=reverse_lazy('logout'))
def register_view(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(username=form.cleaned_data.get('username'),
                            email=form.cleaned_data.get('email'),
                            password=form.cleaned_data.get('password'))
                return redirect(reverse('login'))
            except Exception:
                form.add_error(field='', error='User exists!')

    return render(request, 'register.html', locals())


@login_required(login_url=reverse_lazy('login'))
def logout_view(request):
    logout(request)
    return login_view(request)

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import WordPost, Comment, WordBook
from .forms import WordPostForm, CommentForm, CreateUserForm

# Create your views here.
def index(request):
    posts = WordPost.objects.all().order_by("-pk")
    return render(request, "blog/index.html", {'posts':posts})

@login_required
def new(request):
    if request.method == "POST":
        form = WordPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            wbAdd = WordBook(change_word = request.POST['change_word'], word_mean = request.POST['word_mean'])
            wbAdd.save()
            return redirect('detail', pk=post.pk)
    else:
        form = WordPostForm()
        return render(request, 'blog/new.html', {'form':form})

@login_required
def update(request, pk):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('detail', pk=post.pk)
    else:
        post = get_object_or_404(Post, pk=pk)
        form = PostForm()
    return render(request, 'blog/update.html', {'post':post,'form':form})

@login_required
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.autor:
        post.delete()
        return redirect('main')
    else:
        return redirect('detail', pk=post.pk)

@login_required
def detail_and_add_comment(request, pk):
    post = get_object_or_404(WordPost, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail', pk=post.pk)
    else:
        form = CommentForm()
        okDelete = (request.user == post.author)
    return render(request, 'blog/detail.html', {'post':post,'form': form, 'okDelete':okDelete})

def signup(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            newUser = form.save(commit=False)
            newUser.save()
            return redirect('signup_done')
    else:
        form = CreateUserForm()
    return render(request, 'registration/signup.html', {'form':form})

def signup_done(request):
    return render(request, 'registration/signup_done.html')

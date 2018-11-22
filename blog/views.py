from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by("-pk")
    return render(request, "blog/index.html", {'posts':posts})

def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'blog/new.html', {'form':form})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, "blog/detail.html", {'post':post})

def update(request, pk):
    pass

def delete(request, pk):
    pass

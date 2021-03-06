from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
# from .models import Genre

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_detail_url(request, url):
    post = get_object_or_404(Post, url=url)
    return render(request, 'blog/post_detail.html', {'post': post})

def main_zagl(request):
    post = get_object_or_404(Post, url='main')
    return render(request, 'blog/post_detail.html', {'post': post})

def show_genres(request):
    return render(request, "blog/genres.html", {'genres': Genre.objects.all()})




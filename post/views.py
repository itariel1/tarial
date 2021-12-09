from django.http import HttpResponse
from datetime import datetime

from django.views.generic import CreateView

from . import forms, models
from .models import BlogPost, Comment
from django.shortcuts import render, redirect


# Create your views here.

def hello_world_view(request):
    return HttpResponse('Hello, World!')

def date_view(request):
    now = datetime.now()
    return HttpResponse(str(now))

def blog_view(request):
    posts: list = BlogPost.objects.all()
    # post_info = f"Post title {posts[0].title}." \
    #             f" Post description {posts[0].description}. " \
    #             f"Post likes {posts[0].likes}. " \
    #             # f"Post reposts {posts[0].reposts}"
    # return HttpResponse(post_info)
    return render(request, "blog.html", context={"posts": posts})

def post_detail(request, pk):
    post: BlogPost = BlogPost.objects.get(pk=pk)
    comments = Comment.objects.filter(post_id=pk).order_by("-date")
    return render(request, "blog_detail.html", context={"post": post, "comments": comments})


class BlogCreateView(CreateView):
    template_name = 'blog_create.html'
    form_class = forms.BlogForm
    success_url = '/blog/'
    queryset = models.BlogPost.objects.all()

    def form_valid(self, form):
        return super().form_valid(form=form)

def create_comment(request, pk):
    if request.method == "POST":
        data: dict = request.POST
        post = BlogPost.objects.get(pk=pk)
        comment = Comment.objects.create(text=data['text'], post=post)
        return redirect('post-detail', pk=pk)
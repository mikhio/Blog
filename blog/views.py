from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .utils import ObjectDetailMixim
from .models import Post, Tag

# Create your views here.

def posts_list (request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})

class PostDetail(ObjectDetailMixim, View):
	model = Post
	template = 'blog/post_detail.html'
		

class TagDetail(ObjectDetailMixim, View):
	model = Tag
	template = 'blog/tag_detail.html'
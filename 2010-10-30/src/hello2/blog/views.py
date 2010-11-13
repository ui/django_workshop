# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Post

def home(request):
    
    return render_to_response('home.html', {
        'post_list': Post.objects.all()
    }, RequestContext(request))

def post_detail(request, slug):

    return render_to_response('post_detail.html', {
        'post': Post.objects.get(slug=slug)
    })
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post, Comment
# Create your views here.
def homepage(request):
    allpost = Post.objects.all()
    huvisagch = 'BI CHAMD HAIRTAI'
    commeeeent = Comment.objects.all()
    return render(request, 'index.html', {'a': allpost, 'c': commeeeent})
def about(request):
    return render(request, 'about.html')

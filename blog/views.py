from django.shortcuts import render, get_object_or_404
from .models import Blog


# Create your views here.
def blog(request):
    blogs_limited = Blog.objects.all()[:5]
    return render(request, 'blog/index.html', {'blogs': blogs_limited})


def details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html', {'blog': blog})

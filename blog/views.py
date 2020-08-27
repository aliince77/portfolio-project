from django.shortcuts import render, get_object_or_404
from .models import Blog


def allblogs(request):
    allblogs = Blog.objects.order_by('-pub_date')
    context = {'allblogs': allblogs}
    return render(request, 'blog/allblogs.html', context)


def blogdetail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    context = {'detailblog': detailblog}
    return render(request, 'blog/blog_detail.html', context)

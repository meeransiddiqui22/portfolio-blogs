from django.db.models.base import ModelStateFieldsCacheDescriptor
from blogs.models import Blog
from django.shortcuts import get_object_or_404, render




def all_blogs(request):
    blogs=Blog.objects.all()
    return render(request,'blog/all_blogs.html',{'blogs':blogs})


def details(request,blogs_id):
    blog=get_object_or_404(Blog,pk=blogs_id)
    return render(request,'blog/details.html',{'blog':blog})




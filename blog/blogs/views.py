from django.shortcuts import render,redirect
from .models import code_post,BlogAuthor,Category,example
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def base(request, slug):
    categories = Category.objects.get(slug=slug)
    lists = code_post.objects.filter(publish="publish")
    blogs = code_post.objects.filter(catagory=categories,publish="publish")
    
    print( blogs)
    context = {
        'blogs':blogs,
        'list':lists
    }
    return render(request, 'category.html', context)
def base1(request):
    categories = Category.objects.all()
 
    
    context = {
        'cat':categories
    }
    return render(request, 'base.html', context)

def BlogList(request):
    blog = code_post.objects.filter(publish='publish')

    paginator = Paginator(blog ,12) 

    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
  
        blogs = paginator.page(1)
    except EmptyPage:
    
        blogs = paginator.page(paginator.num_pages)
        
    for i in (blogs):
        i.description=i.description[:500]
    context = {
        'blogs':blogs,
        'blog':blog
    }
    return render(request,'bloglist.html',context)

def BlogDetail(request,slug):
    lis   = code_post.objects.filter(publish="publish")
    blogs = code_post.objects.get(slug=slug,publish="publish")
    examples=example.objects.filter(code_post=blogs)

    print(examples)
  
 
    context = {
        'blogs':blogs,
        'example':examples,
        'list':lis,
      
    }
    return render(request,'blogdetail.html',context)


def BlogAuthors(request):
    authors = BlogAuthor.objects.all()
    context = {
        'authors':authors
    }

    return render(request,'authorlist.html',context)

def BlogListByAuthor(request,id):
    target_author  = BlogAuthor.objects.get(id=id)
    print(target_author)
    blogs          = code_post.objects.filter(author=target_author)
    context = {
        'blogs':blogs,
        'author':target_author
    }
    return render(request,'authorblogs.html',context)




def search(request):

    query=request.GET.get('query',None)
    listing=code_post.objects.filter(publish="publish")
    blogs=code_post.objects.filter(publish="publish")
    if query is not None:
        blogs=blogs.filter(
        Q(title__icontains=query)|
        Q(description__icontains=query)|
        Q(catagory__Name__icontains=query)|
        Q(author__author__username__icontains=query)

        )
    context={

        'blogs':blogs,
        'listing':listing
}

    return render(request,'search.html',context)




def about(request):
    return render(request,'about.html',{})

def privacy(request):
    return render(request,'privacy.html',{})

def affiliations(request):
    return render(request,'affiliations.html',{})

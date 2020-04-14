# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all();
    categories = Post.objects.values('category').distinct();
    context = {
        'judul':'Blog Page',
        'content':'Ini adalah halaman blog website ini',
        'Categories':categories,
        'Posts':posts,
    
    }
    return render(request,'blog/index.html',context)

def detailPost(request,slugInput):
    posts = Post.objects.get(slug=slugInput);
    context = {
        'judul':'Blog Page',
        'content':'Ini adalah halaman blog website ini',
        'Posts':posts,
    
    }
    return render(request,'blog/detail.html',context)
    
def categoryPost(request,categoryInput):
    posts = Post.objects.filter(category=categoryInput);
    categories = Post.objects.values('category').distinct();
    context = {
        'judul':'Blog Page',
        'content':'Menampilkan berdasarkan kategori',
        'Categories':categories,
        'Posts':posts,
    
    }
    return render(request,'blog/category.html',context)
    
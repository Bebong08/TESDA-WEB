from django.db.models import Count, Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView


# from .forms import CommentForm, PostForm
# from .models import Post, Author, PostView
# from marketing.forms import EmailSignupForm
# from marketing.models import Signup


def index(request):
    return render(request, 'index.html',{})

def contact(request):
    return render(request, 'contact.html',{})

def about(request):
    return render(request, 'about.html',{})

def directors(request):
    return render(request, 'directors.html',{})

def structure(request):
    return render(request, 'structure.html',{})

def gallery(request):
    return render(request, 'gallery.html',{})

def compendium(request):
    return render(request, 'compendium.html',{})

def careers(request):
    return render(request, 'careers.html',{})

def news(request):
    return render(request, 'news.html',{})

def centers(request):

    return render(request, 'centers.html',{})

def nttc(request):

    return render(request, 'nttc.html',{})

def assessment_centers(request):

    return render(request, 'assessment_centers.html',{})
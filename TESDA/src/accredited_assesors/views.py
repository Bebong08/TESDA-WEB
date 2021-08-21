from django.shortcuts import render

# Create your views here.


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

def accredited_assesors(request):

    return render(request, 'accredited_assesors.html',{})
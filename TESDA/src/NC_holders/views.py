#from TESDA.src.success_stories.models import Stories
from django.db.models import Count, Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, response
# from .forms import CommentForm, PostForm
# from .models import Post, Author, PostView
# from marketing.forms import EmailSignupForm
# from marketing.models import Signup
from about.models import About
from directors.models import Directors
from gallery.models import Gallery
from news.models import News
from centers.models import Qualifications,Classification
from nttc.models import NTTC
from QMS.models import QMS
from reports.models import Reports
from citizenscharter.models import CitizensReports
from philgeps.models import philG
from assessment_centers.models import Qualifications
from accredited_assesors.models import accredited_assesors
from success_stories.models import Stories
from NC_holders.models import NCHolders
# from .filters import CentersFilter
# from nttc.models import nttc

# class CenterListView(ListView):
#     model = CentersFilter
#     template_name = 'centers.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filter'] = CentersFilter(self.request.Get, queryset=self.get_queryset())
#         return cdontext


# def CenterSearch(request):
#     center_list = News.objects.all()
    

# def search(request):
#     queryset = News.objects.all()
#     query = request.GET.get('q')
#     if query:
#         queryset = queryset.filter(
#             Q(title__icontains=query) |
#             Q(overview__icontains=query)
#         ).distinct()
#     context = {
#         'queryset': queryset
#     }

#     return render(request, 'search_results.html',context)

class SearchView(View):
    def get(self, request, *args, **kwargs):
        queryset = News.objects.all()
        query = request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(overview__icontains=query)
            ).distinct()
        context = {
            'queryset': queryset
        }
        return render(request, 'search_results.html', context)


def search(request):
    queryset = News.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'search_results.html', context)

def index(request):
    latest = News.objects.order_by('-timestamp')[0:3]
    QSS = Directors.objects.order_by('timestamp')[0:1]
    Headline = News.objects.filter(headlines=True)
    Slider = Gallery.objects.filter(slider=True)
    Pics = Gallery.objects.filter(slider=False)
    if request.method =="POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
    
    context ={
        'QS':latest,
        'QSS':QSS,
        'Headline':Headline,
        'Slider':Slider,
        'Pics':Pics
    }
    return render(request, 'index.html',context)

def contact(request):
    return render(request, 'contact.html',{})

def about(request):
    QS = About.objects.all()

    return render(request, 'about.html',{'QS':QS})

def directors(request):
    latest = Directors.objects.order_by('timestamp')[0:1]
    QSS = Directors.objects.all()[1:]

    context = {
        'QSS' : QSS,
        'latest': latest
        
     
    }

    return render(request, 'directors.html',context)

def structure(request):
    return render(request, 'structure.html',{})



def gallery(request):
    QS = Gallery.objects.all()
    return render(request, 'gallery.html',{'QS':QS})

def compendium(request):
    return render(request, 'compendium.html',{})

def careers(request):
    return render(request, 'careers.html',{})

def news(request):
    # latest = News.objects.order_by('-timestamp')[0:1]
    most_recent = News.objects.order_by('-timestamp')[:5]
    QS = News.objects.all()
    paginator = Paginator(QS,2)
    page_request_var = 'page'
    # page = request.Get.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page_request_var)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'QS' : paginated_queryset,
        'most_recent': most_recent,
        # 'latest': latest,
        'page_request_var': page_request_var
     
    }

    return render(request, 'news.html',context)

def centers(request):
   
    # center = Qualifications.objects.order_by('centerclass')
    # joincenter = Qualifications.objects.select_related('Center')
    # centername = joincenter.
   
   if request.method =="POST":
    searchbar = request.POST.get('search_box')
    center = Qualifications.objects.raw('SELECT A.id,B.code,B.description,C.center,CASE WHEN B.status = TRUE THEN "ACTIVE" ELSE "CLOSED" END AS status, E.centertype FROM `centers_qualifications_trainingcenter` A INNER JOIN centers_qualifications B ON A.qualifications_id = B.id INNER JOIN centers_center C ON A.center_id = C.id INNER JOIN centers_qualifications_centerclass D ON B.id = D.qualifications_id INNER JOIN centers_classification E ON D.classification_id = E.id where E.centertype like '+ { search } +'')
    classification = Classification.objects.raw('SELECT centertype FROM centers_classification ORDER BY centers_classification.centertype ASC')
    page_request_var = 'page'
    paginator = Paginator(center, 100)
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
       
        'center':paginated_queryset,
        'classification':classification,
        # 'name':centername
        'page_request_var': page_request_var
    }
    return render(request, 'centers.html',context)
   else:

    center = Qualifications.objects.raw('SELECT A.id,B.code,B.description,C.center,CASE WHEN B.status = TRUE THEN "ACTIVE" ELSE "CLOSED" END AS status, E.centertype FROM `centers_qualifications_trainingcenter` A INNER JOIN centers_qualifications B ON A.qualifications_id = B.id INNER JOIN centers_center C ON A.center_id = C.id INNER JOIN centers_qualifications_centerclass D ON B.id = D.qualifications_id INNER JOIN centers_classification E ON D.classification_id = E.id')
    classification = Classification.objects.raw('SELECT centertype FROM centers_classification ORDER BY centers_classification.centertype ASC')
    page_request_var = 'page'
    paginator = Paginator(center, 100)
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
       
        'center':paginated_queryset,
        'classification':classification,
        # 'name':centername
        'page_request_var': page_request_var
    }
    return render(request, 'centers.html',context)

def nttc(request):
    
    nttc = NTTC.objects.raw('select * from nttc_nttc order by name asc ')
    page_request_var = 'page'
    paginator = Paginator(nttc, 50)
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'nttc':paginated_queryset,
        # 'classification':classification,
        # 'name':centername
        'page_request_var': page_request_var
    }
    return render(request, 'nttc.html',context)

#def registered_workers(request):
 #   return render(request, 'registered_workers.html',{})

def compendium_reports(request):
    CR = Reports.objects.all()
    return render(request, 'compendium_reports.html',{'CR':CR})
    
def organizational_structure(request):
    QS = QMS.objects.all()
    return render(request, 'organizational_structure.html',{'QS':QS})

def news_details(request,id):
    return render(request, 'news_details.html',{})

def citizens_charter(request):
    CC = CitizensReports.objects.all()
    return render(request, 'citizens_charter.html',{'CC':CC})

def PhilGeps(request):
    PG = philG.objects.all()
    return render(request, 'philgeps.html',{'PG':PG})  


def get_news(request, newsid):
    newsx = News.objects.all(newsid)
    response = news.info()
    context = {
        'response':response
    }
    return render(request,'./news_details.html', context)

def assessment_centers(request):
    AC = Qualifications.objects.all()
    return render(request, 'assessment_centers.html',{'AC':AC})  

def accredited_assesor(request):
    AA =  accredited_assesors.objects.all()
    return render(request, 'accredited_assesors.html',{'AA':AA})

def success_stories(request):
    SS =  Stories.objects.all()
    return render(request, 'success_stories.html',{'SS':SS})

def NC_Holders(request):

    return render(request, 'NC_holders.html',{})


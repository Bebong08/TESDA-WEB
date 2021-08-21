
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import View
from django.views.generic.detail import DetailView

# from .views import EGACE, NC_Holders, index, contact, about, directors, search, structure, compendium_reports, citizens_charter, PhilGeps, gallery, careers, news, news_details, centers, nttc, accredited_assesor,organizational_structure,search,assessment_centers,success_stories, scholarship

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('contact/', views.contact),
    path('about/', views.about),
    path('directors/', views.directors),
    path('structure/', views.structure),
    path('centers/', views.centers),
    path('compendium reports/', views.compendium_reports),
    path('gallery/', views.gallery),
    path('careers/', views.careers),
    path('nttc/', views.nttc),
    path('news/', views.news,name='news-list'),
    path('news_details/<id>', views.news_details),
    path('center/', views.centers),
    path('careers/', views.careers),
    path('nttc/', views.nttc),
    path('QMS/',views.organizational_structure),
    path('accredited_assesors/', views.accredited_assesor),
    path('citizens_charter/', views.citizens_charter),
    path('search/', views.search, name='search'),
    path('philgeps/', views.PhilGeps),
    path('assessment_centers/', views.assessment_centers),
    path('success_stories/', views.success_stories),
    path('NC_holders/', views.NC_Holders), 
    path('EGACE/', views.EGACE),
    path('scholarship/', views.scholarship),
    path('testimonials/', views.tTestimonials),
    path('best_practices/', views.pPractices),
    # path('details/<int:pk>/', views.det_Stories, name='details'),
    # url(r'^success_stories/(?P<story_id>\d+)/$', 'det_Stories', name='urlname'),
    # url(r'^search/$', views.CenterSearch, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
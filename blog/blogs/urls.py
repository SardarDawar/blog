from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^about/',views.about,name='about'),
    url(r'^privacy/',views.privacy,name='privacy'),
    url(r'^affiliations/',views.affiliations,name='affiliations'),
    url(r'bloglist',views.BlogList,name='list'),
    url(r'^posts/(?P<slug>[-\w]+)$',views.BlogDetail,name='detail'),
    url(r'^authorlist/',views.BlogAuthors,name='authorlist'),    
    url(r'^author/(?P<id>\d+)$', views.BlogListByAuthor, name="blog-by-author"),
    url(r'^category/(?P<slug>[-\w]+)/$', views.base, name='category'),
    url(r'^cat/', views.base1, name='cat'),
    url(r'^search/',views.search,name='search'),
  

]

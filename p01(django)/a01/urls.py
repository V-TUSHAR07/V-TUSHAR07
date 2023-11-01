from django.contrib import admin
from django.urls import path
from a01 import views

urlpatterns = [
    path('',views.home,name='home'),
    path('a',views.about,name='about'),
    path('a2',views.about2,name='about2'),
    path('cc',views.contact,name='contact'),
    path('b',views.book,name='book'),
    path('blog1',views.blog1,name = "blog1"),
    path('s',views.search,name='search'),
    path('v',views.view, name = 'views'),
    path('v11',views.view11, name = 'views11'),
    path('v44',views.view44, name = 'views44'),
    path('v33',views.view33, name = 'views33'),
    path('v22',views.view22, name = 'views22'),
    path('v2',views.view2, name = 'views2'),
    path('v3',views.view3, name = 'views'),
    path('v4',views.view4, name = 'views')
]
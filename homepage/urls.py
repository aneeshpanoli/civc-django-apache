from django.urls import path, include
from . import views

urlpatterns =[
path('', views.home_view, name='home_view'),
path('es_example/', views.es_example_view, name='es_example_view'),
path('submit/', views.submit_view, name='submit_view'),
path('search_projects/', views.search_projects_view, name='search_projects_view'),
path('home_test/', views.home_test_view, name='home_test_view'),
path('78c3b495-8369-4f1c-abf2-b6142f406b2a/', views.dev_view, name='dev_view'),
]

from django.urls import path, include
from . import views

urlpatterns =[
path('', views.home_view, name='home_view'),
path('es_example/', views.es_example_view, name='es_example_view'),
path('submit/', views.submit_view, name='submit_view'),
path('es_test/', views.es_test_view, name='es_test_view'),
path('home_test/', views.home_test_view, name='home_test_view'),
]

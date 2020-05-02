from django.urls import path, include
from . import views

urlpatterns =[
path('', views.search_index, name='search_view'),
path('test/', views.test_view, name='test_view'),
path('submit/', views.submit_view, name='submit_view'),
]

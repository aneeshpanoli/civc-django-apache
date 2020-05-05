from django.shortcuts import render
from .es_call import esearch, devpost_esearch
# Create your views here.


#========== test views =================================================
def es_example_view(request):
    results = []
    name_term = ""
    gender_term = ""
    if request.GET.get('name') and request.GET.get('gender'):
        name_term = request.GET['name']
        gender_term = request.GET['gender']
    elif request.GET.get('name'):
        name_term = request.GET['name']
    elif request.GET.get('gender'):
        gender_term = request.GET['gender']
    search_term = name_term or gender_term
    results = esearch(firstname = name_term, gender=gender_term)
    # print(results)
    context = {'results': results, 'count': len(results), 'search_term':  search_term}
    return render(request,  'homepage/dev.html',  context)

def search_projects_view(request):
    results = []
    query_term = ""
    if request.GET.get('search_query'):
        query_term = request.GET['search_query']
    elif request.GET.get('browse_category'):
        query_term = request.GET['browse_category']
    # print(request.GET)

    results = devpost_esearch(query_term)
    # print(results)
    context = {'results': results, 'count': len(results), 'search_term':  query_term}
    return render(request,  'homepage/search_project.html',  context)

def home_test_view(request):
    return render(request,  'homepage/index_test.html')

#==================== production views===========================================

def home_view(request):
    return render(request,  'homepage/index.html')

def submit_view(request):
    return render(request,  'homepage/submit-project.html')

from django.shortcuts import render
from .els_es_call import els_update, els_search, els_delete
from .process_airtable import AirtableProcessor

def els_update_view(request):
    results = []
    a_rec = []
    airtable_rec_id = ""
    context = {}
    if request.GET.get('airtable_rec_id'):
        airtable_rec_id = request.GET['airtable_rec_id']
        print(airtable_rec_id)
        airtable = AirtableProcessor('Group submissions')
        try:
            a_rec = airtable.get_a_record(airtable_rec_id)
            results, _ = els_search(airtable_rec_id)
            print(results)
            a_rec = [(a_rec['fields']['recId'], a_rec['fields']['GroupName'], a_rec['fields']['LastUpdated'])]
            context = {'airtable_rec':a_rec + results, 'count': len(results), 'count_a':1 ,'search_term':  airtable_rec_id}
        except:
            context = {'airtable_rec':None,'count': 0, 'count_a':0, 'search_term': None}
    elif request.GET.get('update_record'):
        airtable_rec_id = request.GET['update_record']
        els_update(airtable_rec_id)
        context = {'airtable_rec':None,'count': 0, 'count_a':0, 'search_term': "Updated the record in ELS, Thank you!"}

    elif request.GET.get('delete_record'):
        airtable_rec_id = request.GET['delete_record']
        els_delete(airtable_rec_id)
        context = {'airtable_rec':None,'count': 0, 'count_a':0, 'search_term': "Deleted the record in ELS, Thank you!"}
    return render(request,  'els/els-update.html', context)

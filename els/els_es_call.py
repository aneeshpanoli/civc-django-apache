from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Search, Q
from .split_json import  write_json
from .process_airtable import AirtableProcessor
import os
from django.conf import settings


def els_search(airtable_rec_id):
    client = Elasticsearch()
    q = Q("multi_match", query=airtable_rec_id, fields=['recId'])
    s = Search(using=client, index="submissions").query(q)
    response = s.execute()
    print(f'Total {response.hits.total} hits found.')
    search = get_results(response)
    return search, s

def els_delete(airtable_rec_id):
    _, rec = els_search(airtable_rec_id)
    return rec.delete()

def els_update(airtable_rec_id):
    client = Elasticsearch()
    data = make_data_dict(airtable_rec_id)
    # try to update
    try:
        client.update(index='submissions',doc_type='_doc',id=airtable_rec_id, #hit.meta.id
                    body={"doc": data})
    # if fails create
    except:
        print("couldnt update, id not found, adding to els")
        print(els_ingest(client, airtable_rec_id, data))


def get_results(response):
    results = []
    for hit in response:
        result_tuple = (hit.recId, hit.GroupName,
        hit.LastUpdated)
        results.append(result_tuple)
    return results

def els_ingest(es, airtable_rec_id, data):
    # data = make_data_dict(airtable_rec_id)
    data_dict = {
    '_op_type': 'create',
    '_index': 'submissions',
    '_id': airtable_rec_id,
    'doc': data
    }
    helpers.bulk(es, [data_dict])




def make_data_dict(airtable_rec_id):
    airtable = AirtableProcessor('Group submissions')
    columns = ['recId', 'GroupName', 'Description', 'Status', 'Country',
               'Topics', 'FeaturedImage', 'Resources', 'PrimaryUserAction',
               'CreatedTime', 'City', 'Language', 'Type', 'Sector', 'Organizer',
               'Role', 'TechStack', 'Needs', 'StartDate', 'EndDate', 'LastUpdated']
    data = {i:"" for i in columns}
    a_rec = airtable.get_a_record(airtable_rec_id)
    # print(a_rec)
    for col in a_rec['fields']:
        if col in columns:
            # print(col)
            col_value = a_rec['fields'][col]
            val_append = col_value
            if isinstance(col_value, list):
                rec_table = AirtableProcessor(col)
                val_append = []
                for rec in col_value:
                    if rec.startswith('rec'):
                        col_rec = rec_table.get_a_record(rec)
                        # print(a_rec)
                        val_append.append(col_rec['fields']['Name'])
            data[col] = val_append
    return data

def push_to_els():
    import requests
    headers = {
        'Content-Type': 'application/json',
    }
    params = (
        ('pretty', ''),
        ('refresh', ''),
    )
    data = open(os.path.join(settings.MEDIA_ROOT,'els_update.json'), 'rb').read()
    response = requests.post('http://localhost:9200/submissions/_doc/_bulk', headers=headers, params=params, data=data)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('http://localhost:9200/submissions/_doc/_bulk?pretty&refresh', headers=headers, data=data)

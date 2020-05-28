from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
import json


def esearch(firstname="", gender=""):
    client = Elasticsearch()
    q = Q("bool", should=[Q("match", firstname=firstname),
    Q("match", gender=gender)], minimum_should_match=1)
    s = Search(using=client, index="bank").query(q)[0:20]
    response = s.execute()
    # print('Total {response.hits.total} hits found.')
    search = get_results(response)
    return search

def search_query_dict(query_dict):
    '''
    axios params:
    'params': {
                'q':{
                    'query':{
                        'match_phrase':{
                            'title': searchValue
                        }
                    }
                }
            }
    '''
    client = Elasticsearch()
    results = client.search(index="devpost-2020-04", body=query_dict)
    return results['hits']

def get_results(response):
    results = []
    for hit in response:
        result_tuple = (hit.firstname + ' ' + hit.lastname,
        hit.email, hit.gender, hit.address)
        results.append(result_tuple)
    return results

def devpost_esearch(search_query):
    client = Elasticsearch()
    q = Q("multi_match", query=search_query, fields=['title', 'subtitle', 'storyText'])
    s = Search(using=client, index="devpost-2020-04").query(q)[0:20]
    response = s.execute()
    # print(f'Total {response.hits.total} hits found. Search query: {search_query}')
    search = get_devpost_results(response)
    return search

def get_devpost_results(response):
    results = []
    for hit in response:
        # print(hit)
        result_dict = {"title":hit.title, "image": hit.image, "subtitle":hit.subtitle,
         "text":hit.storyText, "url":hit.url}
        results.append(result_dict)
    return results

def devpost_kw_esearch(key_word):
    client = Elasticsearch()
    q = Q("multi_match", query=key_word, fields=['title', 'subtitleOriginal', 'keywords'])
    s = Search(using=client, index="devpost-2020-04").query(q)[0:20]
    response = s.execute()
    # print('Total {response.hits.total} hits found.')
    search = get_devpost_results(response)
    return search

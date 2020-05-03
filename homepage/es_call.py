from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q


def esearch(firstname="", gender=""):
    client = Elasticsearch()
    q = Q("bool", should=[Q("match", firstname=firstname),
    Q("match", gender=gender)], minimum_should_match=1)
    s = Search(using=client, index="bank").query(q)[0:20]
    response = s.execute()
    print('Total {response.hits.total} hits found.')
    search = get_results(response)
    return search


def get_results(response):
    results = []
    for hit in response:
        result_tuple = (hit.firstname + ' ' + hit.lastname,
        hit.email, hit.gender, hit.address)
        results.append(result_tuple)
    return results

def devpost_esearch(search_query):
    client = Elasticsearch()
    q = Q("multi_match", query=search_query, fields=['title', 'subtitleOriginal', 'storyTextOriginal'])
    s = Search(using=client, index="devpost-2020-04").query(q)[0:20]
    response = s.execute()
    print('Total {response.hits.total} hits found.')
    search = get_devpost_results(response)
    return search

def get_devpost_results(response):
    results = []
    for hit in response:
        result_tuple = (hit.title + ' ' + hit.subtitleOriginal,
        hit.image, hit.storyTextOriginal, hit.url)
        results.append(result_tuple)
    return results

def devpost_kw_esearch(key_word):
    client = Elasticsearch()
    q = Q("multi_match", query=key_word, fields=['title', 'subtitleOriginal', 'keywords'])
    s = Search(using=client, index="devpost-2020-04").query(q)[0:20]
    response = s.execute()
    print('Total {response.hits.total} hits found.')
    search = get_devpost_results(response)
    return search



if __name__ == '__main__':
    print(f"Opal guy details: {esearch(firstname = 'opal')}\n" )
    print(f"the first 20 f gender details:{esearch(gender = 'f')}\n")


import spacy
from collections import Counter
from airtable import Airtable
import pandas as pd
from pathlib import Path
import os
# from google.cloud import translate_v2 as translate
import os
import time

class AirtableHelper:

    def __init__(self):
        self.api_key = 'keyVuEhB1SvC5cDQj'
        self.base_key = 'app4FKBWUILUmUsE1'
        self.main_table_name = 'Groups' # primary database
        self.working_table = 'working_table'
        self.data_path = Path(Path(__file__).resolve().parent, "csv")

    def _is_main_db(self, table_name):
        '''
        Protects the maind db from accidental editing
        '''
        try:
            assert table_name != self.main_table_name
        except AssertionError as e:
            e.args += ("You're Trying to modify the main database! This is dangerous! Terminated!",)
            raise

    def is_working_db(self, table_name):
        try:
            assert table_name != self.working_table
        except AssertionError as e:
            e.args += ("Both working and processing tables are the same! Terminated!",)
            raise

    def fetch_table(self, table_name):
        print("Fetching data from Airtable db '{}'...".format(table_name))
        return Airtable(self.base_key, table_name, api_key=self.api_key)


    def clear_working_db(self, table):
        print("Clearing Airtable db '{}'...".format(self.working_table))
        data = table.get_all()
        for entry in data:
            table.delete(entry['id'])
        print("Clearing finished!".format(self.working_table))

    def to_airtable(self, df):
        working_table = Airtable(self.base_key, self.working_table, api_key=self.api_key)
        self.clear_working_db(working_table)
        print("Writing to Airtable db '{}'...".format(self.working_table))
        for _, row in df.iterrows():
            record=row.to_dict()
            working_table.insert(record)
        print("Writing finished! /n Done!")

# 
# class GoogleTranslate:
#     def __init__(self, cred_path, target):
#         # ptah to your google tranlate api .json credentials file
#         self.set_credentials(cred_path)
#         self.target = 'en'
#         self.translate_client = translate.Client()
#
#     def translate(self, text):
#         """
#         Target must be an ISO 639-1 language code.
#         https://cloud.google.com/translate/docs/languages
#         """
#         time.sleep(3)
#         result = self.translate_client.translate(
#             text,
#             target_language=self.target)
#         return result['translatedText']
#         # print(u'Text: {}'.format(result['input']))
#         # print(u'Translation: {}'.format(result['translatedText']))
#         # print(u'Detected source language: {}'.format(
#         #     result['detectedSourceLanguage']))
#
#     def set_credentials(self, path):
#         os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=path


def get_country(text):
    countries = []
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    for entity in doc.ents:
        if entity.label_ == 'GPE':
            countries.append(entity.text)
    if countries:
        return max(countries, key=countries.count)
    return ''

def get_keywords(text):
    nlp = spacy.load("en_core_web_sm")
    key_words = []
    doc = nlp(text)
    for chunk in doc.noun_chunks:
        key_words.append(chunk.root.text)
    return [a.title() for a, _ in Counter(key_words).most_common(3)]

if __name__ == '__main__':
    t = 'The COVID Tracking Project collects information from 50 US states, \
    the District of Columbia, and 5 other US territories to provide the most\
     comprehensive testing data we can collect for the novel coronavirus, \
     SARS-CoV-2. We currently attempt to include positive and negative results,\
      hospitalizations, and total people tested for each state or district \
      currently reporting that data.'
    # print(extract(t))
    print(get_keywords(t))

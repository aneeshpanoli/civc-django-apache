
# from .helper import GoogleTranslate
from airtable import Airtable
import pandas as pd
from .helper import AirtableHelper



class AirtableProcessor(AirtableHelper):

    def __init__(self, table_name):
        super().__init__()
#         self.run_checks()
#         self.is_working_db(table_name)
        self.table = self.fetch_table(table_name)
        self.table_name = table_name

    def run_checks(self):
        response = input('Before proceeding please make sure the columns names of your \
         table matches with the table at https://airtable.com/tblY84n8azSqbpaux/viwvBcBYXVugRIukX?blocks=show. Poceed? (y/n): ')
        if str(response).lower() != 'y':
            raise ValueError("Your reponse was '{}'. Script terminated!".format(response))

    def get_a_record(self, rec_id):
        return self.table.get(rec_id)

    def to_df(self):
        # coverts airtable to pandas dataframe
        print('Processing {}...'.format(self.table_name))
        record_list = self.table.get_all()
        df = pd.DataFrame([record['fields'] for record in record_list])
        df.fillna("", inplace=True)
        return df

    def df_to_airtable(self, df):
        self.to_airtable(df)

    def df_to_csv(self, df, csv_path):
        df.to_csv(csv_path, index=None, header=True)

    def to_json(self):
        # coverts airtable to pandas dataframe
        print('Processing {}...'.format(self.table_name))
        record_list = self.table.get_all()
        return record_list



if __name__ == '__main__':
    processor = AirtableProcessor('helpwithcovid')
    processor.to_df()

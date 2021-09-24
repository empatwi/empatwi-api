import os
import pandas as pd
from .csv_writer_repository import csv_filename

class CsvTreatmentRepository():

    #TODO: Retornar erro quando o dataframe estiver vazio
    def remove_raw_stream_duplicates(self):
        df = pd.read_csv(os.path.join(csv_filename))
        print(f'Shape before removing duplicates: {df.shape}')

        df_dropped = df.drop_duplicates(subset='tweet_content', keep='first', inplace=False)
        print(f'Shape after removing duplicates: {df_dropped.shape}')

        return df_dropped
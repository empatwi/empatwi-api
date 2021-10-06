import os
import time
import pandas as pd
from .csv_writer_repository import csv_filename

class CsvTreatmentRepository():

    def remove_raw_stream_duplicates(self):
        if os.path.isfile(csv_filename):
            time.sleep(0.5)
            df = pd.read_csv(os.path.join(csv_filename))
            print(f'Shape before removing duplicates: {df.shape}')

            df_dropped = df.drop_duplicates(subset='tweet_content', keep='first', inplace=False)
            print(f'Shape after removing duplicates: {df_dropped.shape}')

            os.remove(os.path.join(csv_filename))

            return df_dropped
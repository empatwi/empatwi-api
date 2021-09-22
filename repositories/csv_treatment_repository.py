import os
import pandas as pd
from .csv_writer_repository import csv_filename

class CsvTreatmentRepository():

    def remove_raw_stream_duplicates(self):
        print(os.path.join(csv_filename))
        df = pd.read_csv(os.path.join(csv_filename))
        print(df.head())

        #pandas.errors.EmptyDataError
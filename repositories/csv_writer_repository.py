import sys
sys.path.append("..")

import csv
import datetime
import os

today = datetime.datetime.today()
today_str = today.strftime('%Y%m%d%H%M%S')
csv_filename = f'files/raw_stream_output_{today_str}.csv'

class CsvWriterRepository():

    def create_csv_file(self):
        csvfile = open(os.path.join(csv_filename), 'a', encoding='utf-8')
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([
            'created_at',
            'tweet_content',
            'keyword',
            'user_location',
            'entities'
        ])

        return csvwriter

    def write_tweets_raw_csv(self, csvwriter, created_at, tweet_content, keyword, user_location, entities):
        """ Writes the csv file that contains raw data from twitter stream output
        """
        csvfile = open(os.path.join(csv_filename), 'a', encoding='utf-8')

        csvwriter.writerow(
            [
                created_at,
                tweet_content,
                keyword,
                user_location,
                entities
            ]
        )

        csvfile.close()

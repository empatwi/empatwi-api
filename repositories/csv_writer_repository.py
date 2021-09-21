import sys
sys.path.append("..")
import csv
import datetime
import os
#from api_routes import keyword

today = datetime.datetime.today()
today_str = today.strftime('%Y%m%d%H%M%S')

csvfile = open(os.path.join(f'files/raw_stream_output_{today_str}.csv'), 'a', encoding='utf-8')
csvwriter = csv.writer(csvfile)
csvwriter.writerow([
    'created_at',
    'tweet_content',
    'keyword',
    'user_location',
    'entities'
])

class CsvWriterRepository():
    
    def set_keyword(self, keyword):
        return keyword

    def write_tweets_raw_csv(self, created_at, tweet_content, keyword, user_location, entities):
         
        csvwriter.writerow(
            [
                created_at,
                tweet_content,
                keyword,
                user_location,
                entities
            ]
        )


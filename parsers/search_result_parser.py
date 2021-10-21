from services.search_service import SearchService

class SearchResultParser():
    
    def search_result_parser(self, keyword):
        positive, negative, positives_explained, negatives_explained = SearchService().search(keyword)
        return {
            "positive": positive,
            "negative": negative,
            "positives_explained": positives_explained,
            "negatives_explained": negatives_explained
        }

    def trending_topics_parser(self, woeid):
        clear_trends = []
        trends = SearchService().trending_topics(woeid)
        trends_list = trends[0]['trends']
        for item in trends_list:
            if item['tweet_volume']:
                trends_dict = {
                    'name': item['name'],
                    'tweet_volume': item['tweet_volume']
                }
            clear_trends.append(trends_dict)
        return clear_trends
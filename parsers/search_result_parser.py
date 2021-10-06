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
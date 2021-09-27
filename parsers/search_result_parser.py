from services.search_service import SearchService

class SearchResultParser():
    
    def search_result_parser(self, keyword):
        positive, negative = SearchService().search(keyword)
        return {
            "positive": positive,
            "negative": negative
        }
def fetch_seo_data(keyword: str) -> dict:
    """
    this function mocks seo data for a given keyword
    """
    
    normalized_keyword = keyword.lower().strip() # normalize keyword for consistent mocking

    # mock data based on a few example keywords
    if "wireless earbuds" in normalized_keyword:
        return {
            "search_volume": 110000,
            "keyword_difficulty": 75,
            "avg_cpc": 1.25
        }
    elif "best laptops" in normalized_keyword:
        return {
            "search_volume": 90500,
            "keyword_difficulty": 80,
            "avg_cpc": 2.10
        }
    elif "healthy recipes" in normalized_keyword:
        return {
            "search_volume": 60500,
            "keyword_difficulty": 65,
            "avg_cpc": 0.90
        }
    else:
        # default mock data for any other keyword
        return {
            "search_volume": 10000 + len(keyword) * 100, # varies by keyword length
            "keyword_difficulty": 50 + len(keyword) % 20, # varies somewhat
            "avg_cpc": 0.50 + (len(keyword) % 5) * 0.1
        }

if __name__ == '__main__':
    # simple test cases for the seo fetcher
    print("SEO Data for 'wireless earbuds':", fetch_seo_data("wireless earbuds"))
    print("SEO Data for 'best laptops':", fetch_seo_data("best laptops"))
    print("SEO Data for 'unique dog names':", fetch_seo_data("unique dog names"))
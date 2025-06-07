# def get_seo_data(keyword):
#     # Mock data
#     return {
#         'search_volume': 2400,
#         'keyword_difficulty': 45,
#         'avg_cpc': 1.25
#     }

# seo_fetcher.py

def fetch_seo_data(keyword: str) -> dict:
    """
    Mocks SEO data for a given keyword.
    In a real-world scenario, this would integrate with an SEO API (e.g., Ahrefs, SEMrush).
    """
    # Normalize keyword for consistent mocking
    normalized_keyword = keyword.lower().strip()

    # Mock data based on a few example keywords
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
        # Default mock data for any other keyword
        return {
            "search_volume": 10000 + len(keyword) * 100, # Varies by keyword length
            "keyword_difficulty": 50 + len(keyword) % 20, # Varies somewhat
            "avg_cpc": 0.50 + (len(keyword) % 5) * 0.1
        }

if __name__ == '__main__':
    # Simple test cases for the SEO fetcher
    print("SEO Data for 'wireless earbuds':", fetch_seo_data("wireless earbuds"))
    print("SEO Data for 'best laptops':", fetch_seo_data("best laptops"))
    print("SEO Data for 'unique dog names':", fetch_seo_data("unique dog names"))
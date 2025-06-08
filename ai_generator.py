import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # loads environment variables from the .env file

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # Initialize the OpenAI client using the API key from environment variables

def generate_blog_post(keyword: str, seo_data: dict) -> str:
    """
    Generates draft blog post using Openai GPT-3.5-turbo model, includes basic structure and placeholder affiliate links, leveraging seo data

    args:
        keyword (str): the primary keyword for the blog post
        seo_data (dict): dictionary containing seo metrics like search_volume, keyword_difficulty, avg_cpc

    returns:
        str: the generated blog post content in markdown format, with affiliate link placeholders replaced by dummy URLs
    """
    # It extract seo insights with default values for robustness
    search_volume = seo_data.get("search_volume", "N/A")
    keyword_difficulty = seo_data.get("keyword_difficulty", "N/A")
    avg_cpc = seo_data.get("avg_cpc", "N/A")

    # this define dummy affiliate links while in a real application, these should typically be managed in a database or a more dynamic configuration
    affiliate_links = {
        "AFF_LINK_1": "https://example.com/affiliate/product1",
        "AFF_LINK_2": "https://example.com/affiliate/product2",
        "AFF_LINK_3": "https://example.com/affiliate/product3",
    }

    # This construct a structured prompt to guide the Openai model, this prompt defines the AI role, the content requirements and integrates the seo data
    prompt_template = f"""
    You are an expert blog post writer specializing in SEO optimized content.
    Generate a detailed and engaging blog post draft about "{keyword}".
    The blog post should be structured with a clear introduction, 2-3 main sections (with subheadings), and a conclusion.
    Incorporate the following SEO insights:
    - Search Volume: {search_volume}
    - Keyword Difficulty: {keyword_difficulty}
    - Average CPC: ${avg_cpc}

    Include at least three placeholder affiliate links, explicitly written as {{AFF_LINK_1}}, {{AFF_LINK_2}}, {{AFF_LINK_3}}, etc., within the body of the post where relevant.
    The tone should be informative and slightly conversational.
    Write the blog post in Markdown format.

    ---
    Blog Post Draft for "{keyword}":

    """

    try:
        # It makes the API call to Openai using 'gpt-3.5-turbo' for efficiency and quality.
        # temperature controls creativity (0.7 is a good balance), max_tokens limits the response length
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates blog posts."},
                {"role": "user", "content": prompt_template}
            ],
            temperature=0.7,
            max_tokens=1500
        )
        blog_content = response.choices[0].message.content

        # this replace ai generated placeholders with actual dummy URLs
        for placeholder, url in affiliate_links.items():
            blog_content = blog_content.replace("{{" + placeholder + "}}", f"[{placeholder}]({url})")

        return blog_content

    except Exception as e:
        print(f"Error generating blog post with OpenAI for '{keyword}': {e}")
        return f"Error generating blog post for '{keyword}': {e}"

if __name__ == '__main__':
    # This block is for standalone testing of this module
    from seo_fetcher import fetch_seo_data # It is immported here to avoid circular dependency if not running app.py

    test_keyword = "sustainable living tips"
    test_seo_data = fetch_seo_data(test_keyword)
    print(f"Generating example blog post for '{test_keyword}' with SEO data: {test_seo_data}")

    generated_post = generate_blog_post(test_keyword, test_seo_data)

    print("\n---------- Generated Blog Post Example ----------")
    print(generated_post)
    print("\n---------- End of Generated Blog Post Example ----------")

    # and it saave the example post to a file, as required for project deliverables
    with open(f"example_{test_keyword.replace(' ', '_')}.md", "w") as f:
        f.write(generated_post)
    print(f"Example post saved to example_{test_keyword.replace(' ', '_')}.md")
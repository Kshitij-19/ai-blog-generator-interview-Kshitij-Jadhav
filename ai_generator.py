# import openai
# import os
# from dotenv import load_dotenv

# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# def generate_blog_post(keyword, seo_data):
#     prompt = f"""
#     Write an SEO-friendly blog post about "{keyword}".
#     Search Volume: {seo_data['search_volume']}, Keyword Difficulty: {seo_data['keyword_difficulty']}, CPC: ${seo_data['avg_cpc']}

#     Include:
#     - Catchy title
#     - Introduction
#     - At least 3 subheadings
#     - Placeholder for affiliate links: {{AFF_LINK_1}}, {{AFF_LINK_2}}
#     - Conclusion
#     """
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=prompt,
#         max_tokens=800
#     )
#     return response.choices[0].text.strip()

# ai_generator.py

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_blog_post(keyword: str, seo_data: dict) -> str:
    """
    Generates a blog post draft using OpenAI's GPT-3.5-turbo model.
    Includes basic structure and placeholder affiliate links.
    """
    search_volume = seo_data.get("search_volume", "N/A")
    keyword_difficulty = seo_data.get("keyword_difficulty", "N/A")
    avg_cpc = seo_data.get("avg_cpc", "N/A")

    # Define dummy affiliate links
    affiliate_links = {
        "AFF_LINK_1": "https://example.com/affiliate/product1",
        "AFF_LINK_2": "https://example.com/affiliate/product2",
        "AFF_LINK_3": "https://example.com/affiliate/product3",
    }

    # Construct the prompt for OpenAI
    prompt_template = f"""
    You are an expert blog post writer specializing in SEO-optimized content.
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
        response = client.chat.completions.create(
            model="gpt-4.1", # You can also use "gpt-4" if you have access and prefer
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates blog posts."},
                {"role": "user", "content": prompt_template}
            ],
            temperature=0.7, # Controls randomness: lower for more focused, higher for more creative
            max_tokens=1500 # Adjust as needed for desired blog post length
        )
        blog_content = response.choices[0].message.content

        # Replace placeholders with actual dummy affiliate links
        for placeholder, url in affiliate_links.items():
            blog_content = blog_content.replace("{{" + placeholder + "}}", f"[{placeholder}]({url})")

        return blog_content

    except Exception as e:
        print(f"Error generating blog post with OpenAI: {e}")
        return f"Error generating blog post for '{keyword}': {e}"

if __name__ == '__main__':
    # Simple test case for AI generator
    from seo_fetcher import fetch_seo_data
    test_keyword = "sustainable living tips"
    test_seo_data = fetch_seo_data(test_keyword)
    print(f"Generating blog post for '{test_keyword}' with SEO data: {test_seo_data}")
    generated_post = generate_blog_post(test_keyword, test_seo_data)
    print("\n--- Generated Blog Post ---")
    print(generated_post)
    print("\n--- End of Generated Blog Post ---")

    # Save an example post for submission
    with open(f"example_{test_keyword.replace(' ', '_')}.md", "w") as f:
        f.write(generated_post)
    print(f"Example post saved to example_{test_keyword.replace(' ', '_')}.md")
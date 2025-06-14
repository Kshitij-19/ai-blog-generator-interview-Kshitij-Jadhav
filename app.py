import os
import json
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import atexit # this makes clean shutdown of background processes

# its custom modules for specific logic
from seo_fetcher import fetch_seo_data
from ai_generator import generate_blog_post

load_dotenv() # loads environment variables from the .env file at application startup

app = Flask(__name__) # initialize the flask application

# blog post generation logic
def create_blog_post_data(keyword: str) -> dict:
    """
    It orchestrates entire blog post generation process anf fetches seo data and then generates the content using the AI module

    args:
        keyword (str): the keyword for which to generate the blog post

    returns:
        dict: A dictionary containing the keyword, seo data, generated content and a timestamp
    """

    seo_data = fetch_seo_data(keyword) # fetch mock seo data

    blog_content = generate_blog_post(keyword, seo_data) # generate the blog post content using the AI generator

    post_data = {
        "keyword": keyword,
        "seo_data": seo_data,
        "blog_post_content": blog_content,
        "generated_at": datetime.now().isoformat() # ISO format for easy parsing and consistency
    } # compile all data into a single dictionary
    return post_data

@app.route('/generate', methods=['GET'])
def generate_post_endpoint():
    """
    This one is API endpoint to generate a blog post based on a provided keyword
    Usage: GET /generate?keyword=<your_keyword>
    Returns: JSON response with blog post data or an error message
    """
    keyword = request.args.get('keyword')

    # basic input validation for the keyword parameter
    if not keyword:
        return jsonify({"error": "Missing 'keyword' parameter. Please provide a keyword like /generate?keyword=your_topic"}), 400

    try:
        # generate the blog post data using the helper function
        post_data = create_blog_post_data(keyword)
        return jsonify(post_data), 200
    except Exception as e:
        # logs the error for internal monitoring
        app.logger.error(f"Error in /generate endpoint for keyword '{keyword}': {e}")
        return jsonify({"error": f"Failed to generate blog post for '{keyword}': {str(e)}."}), 500

# daily Scheduler - APScheduler
def daily_blog_generation_job():
    """
    This function is executed by APScheduler periodically and it generates a blog post for a predefined keyword and saves it to a local file
    """
    
    predefined_keyword = os.getenv("DAILY_KEYWORD", "AI in healthcare") # get predefined keyword from environment variables, with a default fallback
    output_dir = "daily_posts"

    os.makedirs(output_dir, exist_ok=True) # ensure the output directory exists to save generated posts

    print(f"[{datetime.now()}] Running daily blog generation job for keyword: '{predefined_keyword}'")

    try:
        
        post_data = create_blog_post_data(predefined_keyword) # generate the blog post data

        # create a unique, timestamped filename for the generated post
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_keyword = predefined_keyword.replace(' ', '_').replace('/', '_').replace('\\', '_')
        filename = f"{output_dir}/daily_post_{safe_keyword}_{timestamp}.json"

        # saving the generated post data to the json file
        with open(filename, "w") as f:
            json.dump(post_data, f, indent=4) 
        print(f"[{datetime.now()}] Daily post saved to: {filename}")

    except Exception as e:
        print(f"[{datetime.now()}] Error in daily blog generation job: {e}")

scheduler = BackgroundScheduler() # initialize APScheduler. BackgroundScheduler runs tasks in a separate thread

# the daily_blog_generation_job to the scheduler, for demonstration, it's set to run every 1 min
scheduler.add_job(daily_blog_generation_job, 'interval', minutes=1)

# for actual daily use, the 'cron' job will be at a specific hour 
# scheduler.add_job(daily_blog_generation_job, 'cron', hour=3) # runs daily at 3 AM 

# start the scheduler, it will now begin managing the background job
scheduler.start()
print(f"[{datetime.now()}] Scheduler started. Daily job scheduled.")

# makes scheduler shuts down cleanly when the app exits
atexit.register(lambda: scheduler.shutdown())

if __name__ == '__main__':
    
    port = int(os.environ.get('PORT', 5001)) # fetch the port from environment variables, defaulting to 5001

    # 'debug=True' enables helpful development features, 'host='0.0.0.0'' makes the server accessible externally (eg. from other machines on network) 'use_reloader=False' is essential when using APScheduler to prevent duplicate job runs
    app.run(debug=True, host='0.0.0.0', port=port, use_reloader=False)
# from flask import Flask, request, jsonify
# from ai_generator import generate_blog_post
# from seo_fetcher import get_seo_data

# app = Flask(__name__)

# # @app.route('/generate')
# # def generate():
# #     keyword = request.args.get('keyword')
# #     seo_data = get_seo_data(keyword)
# #     blog_post = generate_blog_post(keyword, seo_data)
# #     return jsonify({'keyword': keyword, 'seo': seo_data, 'post': blog_post})

# # if __name__ == '__main__':
# #     app.run(debug=True)

# @app.route('/generate')
# def generate():
#     keyword = request.args.get('keyword')
#     if not keyword:
#         return jsonify({'error': 'Keyword is required'}), 400

#     try:
#         seo_data = get_seo_data(keyword)
#         blog_post = generate_blog_post(keyword, seo_data)
#         return jsonify({'keyword': keyword, 'seo': seo_data, 'post': blog_post})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# app.py

import os
import json
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import atexit

# Import our custom modules
from seo_fetcher import fetch_seo_data
from ai_generator import generate_blog_post

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# --- Blog Post Generation Logic ---
def create_blog_post_data(keyword: str) -> dict:
    """
    Orchestrates the fetching of SEO data and generation of blog post.
    """
    print(f"[{datetime.now()}] Generating blog post for keyword: '{keyword}'")
    seo_data = fetch_seo_data(keyword)
    blog_content = generate_blog_post(keyword, seo_data)

    post_data = {
        "keyword": keyword,
        "seo_data": seo_data,
        "blog_post_content": blog_content,
        "generated_at": datetime.now().isoformat()
    }
    return post_data

# --- API Endpoints ---
@app.route('/generate', methods=['GET'])
def generate_post_endpoint():
    """
    API endpoint to generate a blog post based on a provided keyword.
    Usage: GET /generate?keyword=<your_keyword>
    """
    keyword = request.args.get('keyword')
    if not keyword:
        return jsonify({"error": "Missing 'keyword' parameter."}), 400

    try:
        post_data = create_blog_post_data(keyword)
        return jsonify(post_data), 200
    except Exception as e:
        app.logger.error(f"Error in /generate endpoint for keyword '{keyword}': {e}")
        return jsonify({"error": f"Failed to generate blog post: {str(e)}"}), 500

# --- Daily Scheduler Setup (APScheduler) ---
# Function to be executed by the scheduler
def daily_blog_generation_job():
    predefined_keyword = os.getenv("DAILY_KEYWORD", "AI in healthcare") # Default keyword if not set
    output_dir = "daily_posts"
    os.makedirs(output_dir, exist_ok=True) # Ensure the directory exists

    print(f"[{datetime.now()}] Running daily blog generation job for keyword: '{predefined_keyword}'")
    try:
        post_data = create_blog_post_data(predefined_keyword)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{output_dir}/daily_post_{predefined_keyword.replace(' ', '_').replace('/', '_')}_{timestamp}.json"
        with open(filename, "w") as f:
            json.dump(post_data, f, indent=4)
        print(f"[{datetime.now()}] Daily post saved to: {filename}")
    except Exception as e:
        print(f"[{datetime.now()}] Error in daily blog generation job: {e}")

# Initialize and start the scheduler
scheduler = BackgroundScheduler()
# Schedule the job to run daily at a specific hour (e.g., 3:00 AM)
# Note: For testing, you might want to schedule it to run every few minutes using `minutes=X`
# To run daily, use: scheduler.add_job(daily_blog_generation_job, 'cron', hour=3)
scheduler.add_job(daily_blog_generation_job, 'interval', minutes=1) # For testing: runs every 1 minute
# For actual daily run, uncomment the line below and comment out the above line:
# scheduler.add_job(daily_blog_generation_job, 'cron', hour=3) # Example: runs daily at 3 AM local time

scheduler.start()
print(f"[{datetime.now()}] Scheduler started. Daily job scheduled.")

# Shut down the scheduler when the app exits
atexit.register(lambda: scheduler.shutdown())

# if __name__ == '__main__':
#     # Get port from environment variable, default to 5000
#     port = int(os.environ.get('PORT', 5000))
#     app.run(debug=True, host='0.0.0.0', port=port, use_reloader=False) # use_reloader=False because APScheduler needs to run in a single process

if __name__ == '__main__':
    # Get port from environment variable, default to 5000
    port = int(os.environ.get('PORT', 5001)) # Changed default to 5001
    app.run(debug=True, host='0.0.0.0', port=port, use_reloader=False)
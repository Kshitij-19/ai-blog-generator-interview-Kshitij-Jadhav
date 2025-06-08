# ai-blog-generator-interview-Kshitij-Jadhav

## AI powered blog post generator with daily automation

This project generates AI powered blog post drafts based on a given keyword, incorporates mock seo data and includes a daily automation feature to generate new posts

### project overview

The objective was to create a Flask REST API that interacts with the OpenAI API for content generation, handles environment variables securely, simulates SEO research and implements a robust scheduling mechanism for automated daily content creation. This project showcases practical application of modern backend development principles


### tech stack

* **Python 3.9+**: 
* **Flask**: 
* **OpenAI python client**: 
* **python-dotenv**: 
* **APScheduler**: 

---

### Setup instructions

Follow these steps to get the project up and running

#### 1. Prerequisites

* **Python 3.9+**: Ensure Python is installed. You can check your version with `python3 --version`. Download from [python.org](https://www.python.org/downloads/) if needed
* **VS Code**: Download and install from [code.visualstudio.com](https://code.visualstudio.com/)
* **Git**: Pre installed on macOS
* **OpenAI API Key**: Obtain a secret key from your OpenAI Platform account: [platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys). **Ensure your OpenAI account has sufficient credit or a payment method attached, as the free trial tiers may be limited or expired.**

#### 2. clone the repository

Open your terminal and navigate to your desired development directory. Then, clone the repository:

```bash
git clone [https://github.com/Kshitij-19/ai-blog-generator-interview-Kshitij-Jadhav.git](https://github.com/Kshitij-19/ai-blog-generator-interview-Kshitij-Jadhav.git)
cd ai-blog-generator-interview-Kshitij-Jadhav
```

#### 3. Set up a virtual environment
Set up a virtual environment to manage project dependencies and keep them isolated

```bash
python3 -m venv venv
source venv/bin/activate 
```

#### 4. Install dependencies
Activate virtual environment, install the required Python libraries:

```bash
pip install -r requirements.txt
```

#### 5. Configure environment variables
Create a .env file in the root directory of the project:

Open .env file and add your personal OpenAI API key, I haven't uploaded my key for privacy concers, Also add the keyword for the daily automated post, You can change this to any keyword you prefer for the daily post:

```bash
OPENAI_API_KEY="your_openai_api_key_here"
DAILY_KEYWORD="AI in healthcare"
```

#### 6. Run the application with your virtual environment active
```bash
python app.py
```

For reference, I have added the output which is visible while the app is running

```bash
(venv) (venv) kshitij@Kshitijs-MacBook-Pro Hyperson_Project % python app.py                                                  
[2025-06-06 20:13:56.750581] Scheduler started. Daily job scheduled.
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5001
 * Running on http://10.0.0.14:5001
Press CTRL+C to quit
```


1. Generating a Blog Post via the API
You can interact with the /generate endpoint using web browser or a command line tool like curl

Using a web browser:
```bash
http://localhost:5001/generate?keyword=artificial%20intelligence%20benefits
```
encode url spaces as %20 for keywords with multiple words

Using curl in your terminal:
```bash
curl "http://localhost:5001/generate?keyword=quantum%20computing%20basics" | json_pp
```

The API will return a json response containing the input keyword, mock SEO data and the AI generated blog post content in Markdown format

Sample Output:
```bash
{
  "blog_post_content": "# Artificial Intelligence Benefits: Revolutionizing the Way We Live\n\nIn today's fast-paced world, artificial intelligence (AI) has emerged as a game-changer across various industries. With its ability to mimic human cognitive functions, AI is transforming how we work, interact, and live. Let's delve into the myriad benefits that AI brings to the table.\n\n## Enhancing Efficiency and Productivity\n\nOne of the primary advantages of artificial intelligence is its capability to streamline processes and boost efficiency. AI-powered systems can analyze vast amounts of data at speeds unattainable by humans, leading to quicker and more accurate decision-making. This enhanced efficiency not only saves time but also improves productivity in sectors ranging from healthcare to finance.\n\nMoreover, AI technologies like machine learning enable automation of repetitive tasks, allowing employees to focus on more creative and strategic endeavors. By taking over mundane responsibilities, AI liberates human resources to engage in tasks that require critical thinking and problem-solving skills.\n\nHarnessing AI in business operations can result in significant cost savings and operational enhancements. Companies that adopt AI-driven solutions often experience optimized workflows, reduced errors, and increased output, giving them a competitive edge in today's dynamic market landscape.\n\n## Revolutionizing Customer Experiences\n\nAnother compelling benefit of artificial intelligence lies in its ability to revolutionize customer experiences. AI-powered chatbots, for instance, provide instant and personalized responses to customer queries, enhancing satisfaction and engagement. By leveraging natural language processing and machine learning algorithms, these virtual assistants can understand customer needs and deliver tailored solutions round the clock.\n\nFurthermore, AI facilitates predictive analytics, enabling businesses to anticipate customer preferences and behavior patterns. By analyzing data from past interactions, AI systems can recommend products, services, or content that align with individual interests, thereby enhancing customer loyalty and driving sales.\n\nIn the realm of e-commerce, AI-powered recommendation engines play a pivotal role in guiding purchase decisions. By analyzing browsing history, demographics, and purchase patterns, these systems offer personalized product recommendations, contributing to enhanced user experiences and increased conversion rates.\n\n## Advancing Healthcare and Research\n\nArtificial intelligence has made significant strides in revolutionizing the healthcare industry and advancing scientific research. AI-driven diagnostic tools can analyze medical images, detect anomalies, and assist healthcare professionals in making accurate diagnoses. This not only expedites the diagnostic process but also improves patient outcomes by enabling early detection of diseases.\n\nMoreover, AI algorithms can sift through vast amounts of medical data to identify trends, correlations, and potential treatment options. By leveraging machine learning models, researchers can accelerate drug discovery processes, uncover novel insights, and develop personalized treatment plans tailored to individual patients.\n\nIn the field of genomics, AI plays a crucial role in decoding complex genetic sequences, predicting disease risks, and facilitating precision medicine initiatives. By harnessing AI technologies, scientists can unravel the genetic basis of diseases, paving the way for targeted therapies and personalized healthcare solutions.\n\n## Conclusion\n\nArtificial intelligence is not just a buzzword; it is a transformative force shaping our future. From enhancing efficiency and productivity to revolutionizing customer experiences and advancing healthcare, AI offers a plethora of benefits across diverse domains. As organizations continue to embrace AI technologies, the possibilities for innovation and progress are limitless. Embrace the power of artificial intelligence and unlock a world of opportunities.\n\n---\nIf you're interested in exploring cutting-edge AI solutions for your business, check out {AFF_LINK_1} for a range of AI-powered tools and services. For the latest updates on AI trends and innovations, visit {AFF_LINK_2}. Want to dive deeper into the world of artificial intelligence? Discover insightful resources at {AFF_LINK_3}.",
  "generated_at": "2025-06-06T20:14:10.350776",
  "keyword": "artificial intelligence benefits",
  "seo_data": {
    "avg_cpc": 0.7,
    "keyword_difficulty": 62,
    "search_volume": 13200
  }
}
```
2. Daily scheduler operation

The app.py is configured with APScheduler to run a daily job automatically

For demonstration (current setup): The scheduler is currently set to run every 1 minute for quick verification during development. You will see continuous output in your app.py terminal indicating when the daily job executes:

Sample output:
```bash
[2025-06-06 17:39:52.988784] Running daily blog generation job for keyword: '"AI in healthcare" # Or any other keyword for the daily post'
[2025-06-06 17:39:52.988895] Generating blog post for keyword: '"AI in healthcare" # Or any other keyword for the daily post'
[2025-06-06 17:40:06.173043] Daily post saved to: daily_posts/daily_post_"AI_in_healthcare"_#_Or_any_other_keyword_for_the_daily_post_20250606_174006.json
```

Verifying output: A new json file containing the generated blog post for the DAILY_KEYWORD (e.g., "AI in healthcare") will be saved in the daily_posts/ directory after each scheduled run. Can be verified with ls -l daily_posts/ in a separate terminal.

Production configuration: To switch to actual daily execution like every day at 3 AM local time, please modify app.py by commenting out scheduler.add_job for interval and uncommenting the one for cron:
```bash
scheduler.add_job(daily_blog_generation_job, 'cron', hour=3)
```




<!-- 


# ai-blog-generator-interview-Kshitij-Jadhav

## AI powered blog post generator with daily automation

This project generates AI powered blog post drafts based on a given keyword, incorporates mock seo data and includes a daily automation feature to generate new posts

---

###  Project 0verview

The objective was to create a Flask REST API that interacts with the OpenAI API for content generation, handles environment variables securely, simulates SEO research and implements a robust scheduling mechanism for automated daily content creation. This project showcases practical application of modern backend development principles

---

### Tech stack

* **Python 3.9+**
* **Flask** 
* **OpenAI python client** 
* **python-dotenv**
* **APScheduler**

---

### ⚙️ Setup instructions

#### 1. Prerequisites

* Python 3.9+ ([download python](https://www.python.org/downloads/))
* VS Code ([download VS Code](https://code.visualstudio.com/))
* Git (Pre installed on macOS)
* OpenAI API key ([get API key](https://platform.openai.com/account/api-keys))

#### 2. Clone the repository

```bash
git clone https://github.com/Kshitij-19/ai-blog-generator-interview-Kshitij-Jadhav.git
cd ai-blog-generator-interview-Kshitij-Jadhav
```

#### 3. Set up virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
```

#### 4. Install dependencies

```bash
pip install -r requirements.txt
```

#### 5. Configure environment variables

Create a `.env` file:

```env
OPENAI_API_KEY="your_openai_api_key_here"
DAILY_KEYWORD="AI in healthcare"
```

Ensure `.env` is added to `.gitignore`.

#### 6. Run the Flask App

```bash
python app.py
```

You should see output like:

```
[2025-06-06 20:13:56] Scheduler started. Daily job scheduled.
 * Running on http://127.0.0.1:5001
```

---

### 🕹️ How to Use

#### 1. Generate a Blog Post via API

**Using a browser**:

```
http://localhost:5001/generate?keyword=artificial%20intelligence%20benefits
```

**Using curl**:

```bash
curl "http://localhost:5001/generate?keyword=quantum%20computing%20basics" | json_pp
```

You will receive a JSON response containing the blog post content in Markdown, the input keyword, and mock SEO metrics.

#### 2. Daily Scheduler Operation

* **For Development**: Scheduler runs every 1 minute (set via APScheduler in `app.py`)
* **For Production**: Change to:

```python
scheduler.add_job(daily_blog_generation_job, 'cron', hour=3)
```

**Sample Output**:

```
[2025-06-06 17:40:06] Daily post saved to: daily_posts/daily_post_AI_in_healthcare_20250606_174006.json
```

To view all generated posts:

```bash
ls -l daily_posts/
```

---

### 📄 Sample Output

Example response JSON:

```json
{
  "keyword": "artificial intelligence benefits",
  "seo_data": {
    "search_volume": 13200,
    "keyword_difficulty": 62,
    "avg_cpc": 0.7
  },
  "blog_post_content": "# Artificial Intelligence Benefits...",
  "generated_at": "2025-06-06T20:14:10"
}
```

Blog posts contain:

* SEO-friendly title
* Structured content with subheadings
* Affiliate placeholders like `{AFF_LINK_1}`
* Written in Markdown format

---

### 📆 Project Deliverables

| Component                      | Status |
| ------------------------------ | ------ |
| Flask API `/generate` endpoint | ✅      |
| Mock SEO fetcher               | ✅      |
| OpenAI integration             | ✅      |
| Markdown blog generation       | ✅      |
| Daily automation (APScheduler) | ✅      |
| Example blog output            | ✅      |
| `.env` + Git ignore            | ✅      |
| Clean README                   | ✅      |
| GitHub Repo Ready              | ✅      |

---

### 🚀 Final Notes

* Keep OpenAI usage under rate limits.
* Secure `.env` file.
* Prompt engineering impacts quality.
* To switch affiliate placeholders, replace `{AFF_LINK_n}` with actual URLs.

---

**Good luck and happy blogging!** -->

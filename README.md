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

daily_posts/daily_post_"AI_in_healthcare"_#_Or_any_other_keyword_for_the_daily_post_20250607_223240.json has scheduler output which runs every 1 minute. Added the output form that file below, it ran for keyword "AI in healthcare":

```bash
{
    "keyword": "\"AI in healthcare\" # Or any other keyword for the daily post",
    "seo_data": {
        "search_volume": 16000,
        "keyword_difficulty": 50,
        "avg_cpc": 0.5
    },
    "blog_post_content": "# The Impact of AI in Healthcare: Revolutionizing the Future of Medicine\n\nIn recent years, Artificial Intelligence (AI) has made significant strides in transforming various industries, and healthcare is no exception. The integration of AI technologies in healthcare has the potential to revolutionize the way medical professionals diagnose, treat, and manage patient care. Let's delve into the role of AI in healthcare and explore how this cutting-edge technology is reshaping the future of medicine.\n\n## Advancements in Diagnostics and Disease Management\n\nOne of the most notable applications of AI in healthcare is in diagnostics and disease management. AI algorithms can analyze vast amounts of medical data, such as patient records, lab results, and imaging scans, to identify patterns and trends that may not be apparent to human healthcare providers. This ability to process and interpret data quickly and accurately can lead to earlier and more accurate diagnoses, ultimately improving patient outcomes.\n\nFurthermore, AI-powered predictive analytics can help healthcare professionals anticipate potential health issues and intervene proactively. By leveraging AI algorithms to analyze patient data and identify risk factors, medical professionals can develop personalized treatment plans and preventive strategies tailored to individual patients' needs.\n\n## Enhanced Patient Care and Treatment Optimization\n\nAI technologies are also revolutionizing patient care and treatment optimization by streamlining processes and improving efficiency. For instance, AI-powered chatbots and virtual assistants can provide patients with instant access to healthcare information, answer medical queries, and schedule appointments, enhancing overall patient experience and engagement.\n\nMoreover, AI-driven treatment optimization tools can assist healthcare providers in selecting the most effective treatment options for patients. By analyzing vast amounts of data on treatment outcomes and patient responses, AI algorithms can recommend personalized treatment plans that are more likely to succeed, leading to better patient care and improved treatment outcomes.\n\n## Ethical Considerations and Future Implications\n\nWhile the integration of AI in healthcare offers numerous benefits, it also raises ethical considerations and challenges. Issues such as data privacy, security, and algorithm bias must be carefully addressed to ensure that AI technologies are used responsibly and ethically in healthcare settings.\n\nLooking ahead, the future implications of AI in healthcare are vast and promising. From precision medicine and personalized healthcare to predictive analytics and remote patient monitoring, AI has the potential to transform the way we approach healthcare delivery and improve patient outcomes on a global scale.\n\nIn conclusion, the integration of AI in healthcare is revolutionizing the future of medicine by enhancing diagnostics, optimizing treatment, and improving patient care. As AI technologies continue to evolve and advance, the healthcare industry is poised to benefit from increased efficiency, accuracy, and innovation in delivering quality healthcare services to patients worldwide.\n\n---\nDon't miss out on the latest advancements in AI-driven healthcare solutions. Stay informed and explore cutting-edge technologies in medical diagnostics and patient care with {AFF_LINK_1}. Embrace the future of healthcare today!\n\nWould you like to learn more about how AI is transforming the healthcare industry? Discover the potential of AI-driven treatment optimization and personalized healthcare solutions with {AFF_LINK_2}. Join the revolution in healthcare technology!\n\nReady to explore the ethical implications and future implications of AI in healthcare? Dive deeper into the ethical considerations surrounding AI integration in healthcare and envision the future of medicine with {AFF_LINK_3}. Stay ahead of the curve in healthcare innovation!",
    "generated_at": "2025-06-07T22:32:40.953619"
}
```

Also added the deliverable (2), which is final blog post generated in file example_sustainable_living_tips.md
Output from that file:

```markdown
# Sustainable Living Tips: How to Live Sustainably Every Day

In a world where environmental concerns are becoming increasingly urgent, adopting sustainable living practices is crucial. Not only does sustainable living benefit the planet, but it also promotes a healthier lifestyle and helps to save money in the long run. If you're looking to make a positive impact on the environment and reduce your carbon footprint, here are some practical tips to help you live more sustainably every day.

## 1. Reduce, Reuse, Recycle

### Reduce Waste:
One of the fundamental principles of sustainable living is to minimize waste. Start by avoiding single-use plastics and opting for reusable alternatives such as stainless steel water bottles, cloth shopping bags, and glass food containers. By reducing your consumption of disposable items, you can significantly cut down on the amount of waste that ends up in landfills.

### Reuse Items:
Instead of throwing away items that are still in good condition, consider finding new uses for them. Repurpose old jars as storage containers, turn worn-out clothes into cleaning rags, or donate unwanted items to charity. Embracing a culture of reuse not only reduces waste but also encourages creativity and resourcefulness.

### Recycle Responsibly:
Recycling plays a vital role in sustainable living by diverting materials from landfills and conserving natural resources. Familiarize yourself with your local recycling guidelines to ensure that you are sorting and disposing of recyclable materials correctly. Look for products made from recycled materials and support companies that prioritize sustainability in their production processes.

{AFF_LINK_1}

## 2. Embrace Energy Efficiency

### Conserve Electricity:
Reduce your energy consumption by unplugging electronics when they are not in use, switching to energy-efficient appliances, and installing LED light bulbs. Consider investing in a programmable thermostat to optimize your home's heating and cooling systems, thereby reducing energy waste and lowering your utility bills.

### Harness Renewable Energy:
Explore renewable energy options such as solar panels or wind turbines to power your home with clean, sustainable energy. While the initial cost of these systems may be higher, the long-term benefits in terms of energy savings and environmental impact make them a worthwhile investment for eco-conscious individuals.

### Practice Water Conservation:
Save water by fixing leaks, taking shorter showers, and installing low-flow fixtures in your home. Collect rainwater for outdoor irrigation and consider xeriscaping – landscaping that requires minimal water – to create a more sustainable garden. Being mindful of your water usage not only conserves a precious resource but also reduces the energy required for water treatment and distribution.

{AFF_LINK_2}

## 3. Support Sustainable Brands and Practices

### Choose Ethical Products:
When shopping for goods, opt for products that are ethically sourced, cruelty-free, and environmentally friendly. Look for certifications such as Fair Trade, USDA Organic, or Forest Stewardship Council (FSC) to ensure that your purchases support sustainable practices and responsible production methods.

### Reduce Meat Consumption:
The meat industry is a significant contributor to greenhouse gas emissions and deforestation. Consider incorporating more plant-based meals into your diet to reduce your carbon footprint and promote animal welfare. By supporting sustainable agriculture and ethical food production, you can make a positive impact on both your health and the environment.

### Engage in Community Initiatives:
Get involved in local sustainability efforts by volunteering at community gardens, participating in beach cleanups, or attending environmental awareness events. By connecting with like-minded individuals and supporting grassroots initiatives, you can amplify your impact and contribute to a more sustainable future for your community.

{AFF_LINK_3}

## Conclusion

Living sustainably is not just a trend – it's a responsible way of life that benefits both the planet and future generations. By incorporating these sustainable living tips into your daily routine, you can make a meaningful difference and inspire others to join you on the journey towards a greener, more sustainable world. Remember, even small changes can have a big impact when it comes to protecting our environment and creating a brighter future for all.

Start your sustainable living journey today and be the change you wish to see in the world!

---
*Search Volume: 12300*
*Keyword Difficulty: 53*
*Average CPC: $0.8*
```

This blog post draft provides comprehensive tips on sustainable living, covering areas such as waste reduction, energy efficiency, and supporting sustainable brands. By following these practical suggestions, readers can take meaningful steps towards living a more eco-friendly and sustainable lifestyle.


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

# from apscheduler.schedulers.background import BackgroundScheduler
# from ai_generator import generate_blog_post
# from seo_fetcher import get_seo_data
# import datetime

# def scheduled_task():
#     keyword = "wireless earbuds"
#     seo = get_seo_data(keyword)
#     post = generate_blog_post(keyword, seo)
#     with open(f"{keyword.replace(' ', '_')}_{datetime.date.today()}.md", "w") as f:
#         f.write(post)

# def start_scheduler():
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(scheduled_task, 'interval', days=1)
#     scheduler.start()
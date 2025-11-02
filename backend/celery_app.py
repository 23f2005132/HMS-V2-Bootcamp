from celery import Celery

# initialize Celery application
celeryApp = Celery(
    'tasks',
    broker='redis://localhost:6379/0'
)

# Optional: Configure Celery settings
celeryApp.conf.update(
    timezone='Asia/Kolkata',
    enable_utc=False,
)

# tasks

from mail import send_email
from app import app
from models import User

@celeryApp.task()
def daily_reminder():
    print('started daily reminders')
    with app.app_context():
        for user in User.query.all():
            to = user.email
            subject = "Daily Reminder"
            body = f"Hello {user.name}, this is your daily reminder to visit out application."
            send_email(to, subject, body)
    return "Daily reminders sent!"

@celeryApp.task()
def monthly_newsletter():

    with app.app_context():
        for user in User.query.all():
            to = user.email
            subject = "Monthly Newsletter"
            body = f"Hello {user.name}, welcome to our monthly newsletter!"
            send_email(to, subject, body)
    return "Monthly newsletters sent!"

@celeryApp.task()
def export_csv(email):
    import time
    time.sleep(30)
    # Placeholder for CSV export logic
    # This function would contain the logic to export data to a CSV file
    to = email
    subject = "CSV export done"
    body = """<a href="http://127.0.0.1:5000/static/export_file.csv">Click here to download file</a>"""
    send_email(to, subject, body)
    return "CSV export completed!"


# schedule tasks
from celery.schedules import crontab
import datetime

celeryApp.conf.beat_schedule = {
    'daily_reminders': {
        'task': 'celery_app.daily_reminder',
        'schedule': crontab(hour=16, minute=53) # every day
        # 'schedule': datetime.timedelta(seconds=3) # every 3 seconds
    },
    'montly_reminders': {
        'task': 'celery_app.monthly_reminder',
        'schedule': crontab(day_of_month=2, hour=16, minute=30)
    }
}
import smtplib
from email.mime.text import MIMEText

SMTP_HOST = 'localhost'
SMTP_PORT = 1025
FROM_EMAIL = 'admin@gmail.com'

def send_email(to_email, subject, body):
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = FROM_EMAIL
    msg['To'] = to_email

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.sendmail(FROM_EMAIL, [to_email], msg.as_string())




if __name__ == "__main__":

    from app import app
    from models import User

    with app.app_context():
        print("Sending test emails to all users...")

        for user in User.query.all():

            to = user.email

            html = """\
            <html>
            <body style="font-family: Arial, sans-serif; background:#f6f9fc; margin:0; padding:20px;">
                <div style="max-width:600px; margin:0 auto; background:#ffffff; border-radius:8px; overflow:hidden; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
                <div style="background:#4a90e2; color:#ffffff; padding:20px 24px;">
                    <h1 style="margin:0; font-size:20px;">Testing Email</h1>
                    <p style="margin:4px 0 0; font-size:14px; opacity:0.95;">Beautiful HTML UI</p>
                </div>
                <div style="padding:24px; color:#333333; line-height:1.5; font-size:15px;">
                    <p>Hello,</p>
                    <p>This is a test email sent from the local SMTP server. It uses a simple, clean HTML layout with inline styles so most mail clients render it correctly.</p>
                    <div style="text-align:center; margin:20px 0;">
                    <a href="#" style="display:inline-block; background:#4a90e2; color:#ffffff; text-decoration:none; padding:10px 18px; border-radius:6px; font-weight:600;">View Details</a>
                    </div>
                    <p style="color:#666666; font-size:13px;">If you did not expect this email, you can ignore it.</p>
                </div>
                <div style="background:#f2f6fb; color:#6b7280; padding:12px 24px; font-size:13px;">
                    Sent by Admin &middot; <span style="opacity:0.9">admin@example.com</span>
                </div>
                </div>
            </body>
            </html>
            """

            send_email(to, "Test: Beautiful HTML Email", html)

            print("Test email sent to", to)
from celery import shared_task
from django.core.mail import send_mail
import time

@shared_task
def send_welcome_email_task(email_address):
    # Simulating a slow operation (like contacting an SMTP server)
    time.sleep(5) 
    
    send_mail(
        subject='Welcome to the Library!',
        message='Thanks for signing up. Enjoy your books.',
        from_email='noreply@library.com',
        recipient_list=[email_address],
        fail_silently=False,
    )
    return f"Email sent to {email_address}"
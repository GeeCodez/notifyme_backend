from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_email(email,reference):
    send_mail(
        subject="Booking confirmation",
        message=f"Your booking {reference} is confirmed",
        from_email=None,
        recipient_list=[email],
        fail_silently=False
    )
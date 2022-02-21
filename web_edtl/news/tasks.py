from celery import shared_task
from time import sleep
from django.core.mail import send_mail, EmailMessage,EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from django.template.loader import render_to_string
from email.mime.image import MIMEImage
from django.contrib.staticfiles import finders
import os

@shared_task
def send_email(subject,template, email_from, email_to):

   
    email = EmailMessage(
        subject,
        template,
        email_from,
        [email_to]
    )
    email.fail_silently= False
    email.content_subtype = "html"
    email.send()
    return None

@shared_task
def new_news(email_to,to_email, title):
    subject = 'News Notification'
    body_html = render_to_string('email/send.html',{'to_email': to_email, 'title': title})
    from_email = settings.EMAIL_HOST_USER
    msg = EmailMultiAlternatives(
        subject,
        body_html,
        from_email=from_email,
        to=[email_to]
    )
    msg.attach_alternative(body_html, "text/html")
    msg.send()
    return None

@shared_task
def new_subs(email_to,to_email, url):
    subject = 'Email Confirmation'
    body_html = render_to_string('email/new_sub.html',{'to_email': to_email, 'url': url})
    from_email = settings.EMAIL_HOST_USER
    msg = EmailMultiAlternatives(
        subject,
        body_html,
        from_email=from_email,
        to=[email_to]
    )
    msg.attach_alternative(body_html, "text/html")
    msg.send()
    return None
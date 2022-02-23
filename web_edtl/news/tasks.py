from celery import shared_task
from time import sleep
from django.core.mail import send_mail, EmailMessage,EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
import os
from django.http import HttpResponse
import requests
import json
from django.templatetags.static import static

image_url = static('main/img/logo.png')

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
def send_event(email_to,to_email, title):
    subject = 'Event Notification'
    body_html = render_to_string('email/event.html',{'to_email': to_email, 'title': title})
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
def send_announcement(email_to,to_email, title):
    subject = 'Announcement Notification'
    body_html = render_to_string('email/announcement.html',{'to_email': to_email, 'title': title})
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
def send_vacancy(email_to,to_email, title):
    subject = 'Vacancy Notification'
    body_html = render_to_string('email/announcement.html',{'to_email': to_email, 'title': title})
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
def send_tender(email_to,to_email, title):
    subject = 'Tender Notification'
    body_html = render_to_string('email/tender.html',{'to_email': to_email, 'title': title})
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


def send_notification(registration_ids , message_title , message_desc, image):
    fcm_api = "AAAA79BRMps:APA91bFy0m7nCsQslCnlJQVFF3ubHfaVPy1lmrF-Hr2vUk-bOCdcZJLC7DR86T2LBz1ndVNC9eB6grmQOLg1RRMEB2V54MFtXCmrTVWd_953iS_Wc-Cdnf1dtALuCma1tCMVBxr6s8uk"
    url = "https://fcm.googleapis.com/fcm/send"
    
    headers = {
    "Content-Type":"application/json",
    "Authorization": 'key='+fcm_api}

    payload = {
        "registration_ids" :registration_ids,
        "priority" : "high",
        "notification" : {
            "body" : message_desc,
            "title" : f"News: {message_title}",
            "image" : image.url,
            "icon": image_url
            
        }
    }

    result = requests.post(url,  data=json.dumps(payload), headers=headers )
    print(result.json())

def send_tender_notification(registration_ids , message_title , message_desc, image):
    fcm_api = "AAAA79BRMps:APA91bFy0m7nCsQslCnlJQVFF3ubHfaVPy1lmrF-Hr2vUk-bOCdcZJLC7DR86T2LBz1ndVNC9eB6grmQOLg1RRMEB2V54MFtXCmrTVWd_953iS_Wc-Cdnf1dtALuCma1tCMVBxr6s8uk"
    url = "https://fcm.googleapis.com/fcm/send"
    
    headers = {
    "Content-Type":"application/json",
    "Authorization": 'key='+fcm_api}

    payload = {
        "registration_ids" :registration_ids,
        "priority" : "high",
        "notification" : {
            "body" : message_desc,
            "title" : f"Tender: {message_title}",
            "image" : image.url,
            "icon": image_url
            
        }
    }

    result = requests.post(url,  data=json.dumps(payload), headers=headers )
    print(result.json())

def send_announcement_notification(registration_ids , message_title , message_desc, image):
    fcm_api = "AAAA79BRMps:APA91bFy0m7nCsQslCnlJQVFF3ubHfaVPy1lmrF-Hr2vUk-bOCdcZJLC7DR86T2LBz1ndVNC9eB6grmQOLg1RRMEB2V54MFtXCmrTVWd_953iS_Wc-Cdnf1dtALuCma1tCMVBxr6s8uk"
    url = "https://fcm.googleapis.com/fcm/send"
    
    headers = {
    "Content-Type":"application/json",
    "Authorization": 'key='+fcm_api}

    payload = {
        "registration_ids" :registration_ids,
        "priority" : "high",
        "notification" : {
            "body" : message_desc,
            "title" : f"Announcement: {message_title}",
            "image" : image.url,
            "icon": image_url
            
        }
    }

    result = requests.post(url,  data=json.dumps(payload), headers=headers )
    print(result.json())

def send_vacancy_notification(registration_ids , message_title , message_desc, image):
    fcm_api = "AAAA79BRMps:APA91bFy0m7nCsQslCnlJQVFF3ubHfaVPy1lmrF-Hr2vUk-bOCdcZJLC7DR86T2LBz1ndVNC9eB6grmQOLg1RRMEB2V54MFtXCmrTVWd_953iS_Wc-Cdnf1dtALuCma1tCMVBxr6s8uk"
    url = "https://fcm.googleapis.com/fcm/send"
    
    headers = {
    "Content-Type":"application/json",
    "Authorization": 'key='+fcm_api}

    payload = {
        "registration_ids" :registration_ids,
        "priority" : "high",
        "notification" : {
            "body" : message_desc,
            "title" : f"Vacancy: {message_title}",
            "image" : image.url,
            "icon": image_url
            
        }
    }

    result = requests.post(url,  data=json.dumps(payload), headers=headers )
    print(result.json())



from time import sleep
from celery import shared_task
# it coupled celery to app
# from storefront.celery import celery
# @celery.task

@shared_task
def notify_customer(message):
    print('Sending 10k email')
    print(message)
    sleep(10)
    print('Emails successfully sent!')
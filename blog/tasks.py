from celery import shared_task
from celery.schedules import crontab
from django.conf import settings
from django.core.mail import send_mail
from app_site.celery import app
from blog.models import Post


@app.task
def send_email():
    send_mail(
        subject='Тема',
        message='Сообщение',
        from_email=settings.EMAIL_HOST_USER,    # от кого
        recipient_list=['bulat.kajrov@yandex.ru'],  # куда/кому
        fail_silently=False,
    )


@shared_task
def send_all_posts():
    posts = Post.objects.all()
    msg = [f'Заголовок:{post.title}\nтекст{post.content}\nавтор{post.author}' for post in posts]
    message = '\n'.join(msg)
    send_mail(
        subject='Тема',
        message=message,
        from_email=settings.EMAIL_HOST_USER,  # от кого
        recipient_list=['bulat.kajrov@yandex.ru'],  # куда/кому
        fail_silently=False,
    )


app.conf.beat_schedule = {
    'send_spam_every_1_min': {
        'task': 'blog.tasks.send_all_posts',
        'schedule': crontab(minute='*/1')
    }
}

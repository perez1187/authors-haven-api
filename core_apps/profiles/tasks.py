from celery import shared_task

from .models import Profile


@shared_task
def add(id):
    profile = Profile.objects.get(pkid=2)
    profile.about_me = "done"
    profile.save()

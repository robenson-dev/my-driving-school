from django.db.models.signals import post_save
from users.models import User, Instructor, Student
from Student.models import Subscription
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_instructor(sender, instance, created, **kwargs):
    if created:
        if instance.is_instructor == True:
            Instructor.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_instructor(sender, instance, created, **kwargs):
    if created:
        if instance.is_student == True:
            Student.objects.create(user=instance)
            Subscription.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_instructor(sender, instance, created, **kwargs):
#     instance.instructor.save()

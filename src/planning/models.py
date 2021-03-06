from django.db import models
from users.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField


class Event(models.Model):

    start = models.DateTimeField('start', db_index=True)
    end   = models.DateTimeField('end', db_index=True, help_text="The end time must be later than the start time.")
    title = models.CharField('title', max_length=255)
    description = RichTextField("description", blank=True)
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="creator",
        related_name='snippets'
    )
    person = models.OneToOneField(User,
        blank=True,
        verbose_name="person",
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField("created on", auto_now_add=True)
    updated_on = models.DateTimeField("updated on", auto_now=True)
    color_event = ColorField("Color event", blank=True, max_length=10, default='#FFC0CB')
    address = models.CharField(max_length=255, blank=True)

    def get_absolute_url(self):
        return reverse('secretary:appointment-detail',kwargs={'pk':self.pk})

    class Meta:
        verbose_name = "event"
        verbose_name_plural = "events"
        index_together = (("start", "end"),)

    def __str__(self):
        return self.title

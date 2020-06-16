from django.db import models
from django.utils import timezone

# Create your models here.
class Formdemo(models.Model):
    text = models.TextField('備考', blank=True)

    def __str__(self):
        return self.text


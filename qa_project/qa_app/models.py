

# Create your models here.
from django.db import models

class QA(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

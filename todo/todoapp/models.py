from django.db import models

# Create your models here.
# models for the db


class Task(models.Model):
    task_name = models.CharField(max_length=200)
    task_prioritiy = models.CharField(max_length=200)
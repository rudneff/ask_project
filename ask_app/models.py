from django.db import models
import datetime


class Questions(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0, db_index=True)
    created = models.DateTimeField(default=datetime.datetime.now)


class QuestionManager(models.Model):
    def newest(self):
        return self.order_by('-id')
# Create your models here.

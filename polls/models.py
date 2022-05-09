import datetime

from django.db import models
from django.utils import timezone

#Two Tables
class Question(models.Model):
    question_text = models.CharField(max_length=200) #field(column)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #Foreign Key to Question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

# Make chage to models 3 steps guide
#   Change your models (in models.py).
#   Run python manage.py makemigrations to create migrations for those changes
#   Run python manage.py migrate to apply those changes to the database.
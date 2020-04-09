from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(unique=True, max_length=255)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.email)

class Level(models.Model):
    name = models.CharField(max_length=255)
    enabled = models.BooleanField(default=False)
    seq = models.IntegerField(default=0)

    def __str__(self):
        return '{} - {}'.format(self.name, self.enabled)

class Category(models.Model):
    name = models.CharField(max_length=255)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.name, self.enabled)

class Question(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='questions')
    question = models.TextField()

    def __str__(self):
        return '{}'.format(self.question)

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    option = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.option, 'Correct' if self.is_correct else 'Incorrect')

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    category = models.ForeignKey(
         Category, 
         on_delete=models.CASCADE
    )
    score = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {} {} {}'.format(self.user.name, self.level.name, self.category.name, self.score)

class Attempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    attempts = models.IntegerField()
    attempts_remaining = models.IntegerField(default=5)

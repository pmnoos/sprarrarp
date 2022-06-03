from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


EXPERTISE_CHOICES = [
    ('BEG', 'have not been on a horse'),
    ('INT', 'have been on a horse but feel unsure'),
    ('ADV', 'can ride a horse when it walks'),
    ('EXP', 'can ride a horse in all speeds'),
    ('PRO', 'Professional'),
]
GALLOP_CHOICES = [
    ('EVE', 'Everyone in group wants to Gallop'),
    ('FEW', 'Few in group want to Gallop'),
    ('NOB', 'Nobody in group wants to Gallop'),
    ('WAL', 'We only want to walk on the horses'),
]
SNACK_CHOICES = [
    ('0KR', 'No Snacks'),
    ('50KR', 'Coffee-saft-buns'),
    ('100KR', 'Coffes-aft-buns-princess-cake'),
]


class Individual(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    comments = models.TextField(max_length=100)
    age = models.IntegerField()
    weight = models.IntegerField()
    experience = models.CharField(choices=EXPERTISE_CHOICES, max_length=3)
    gallop = models.CharField(choices=GALLOP_CHOICES, max_length=30, default='Nobody')
    snacks = models.CharField(choices=SNACK_CHOICES, max_length=50, default='None')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

EXPERTISE_CHOICES = [
    ('BEG', 'have not been on a horse'),
    ('INT', 'have been on a horse but feel unsure'),
    ('ADV', 'can ride a horse when it walks'),
    ('EXP', 'can ride a horse in all speeds'),
    ('PRO', 'Professional'),
]
class Member(models.Model):
    rider = models.IntegerField()
    date = models.DateTimeField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    weight = models.IntegerField()
    experience = models.CharField(choices=EXPERTISE_CHOICES, max_length=3)
    comments = models.TextField(max_length=100)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name


class EventInfo(models.Model):
    date = models.DateTimeField()
    capacity = models.IntegerField()
    registered = models.IntegerField()
    available = models.IntegerField()
    cancel_date = models.DateTimeField()        
    price = models.IntegerField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.location
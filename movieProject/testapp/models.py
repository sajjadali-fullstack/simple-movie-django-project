from django.db import models

# Create your models here👇.

# rdate, moviename, hero, heroin, rating

# Python code ==> SQL ==> Executed --> Table(DB)
# 1.python manage.py makemigrations  ==> it convertes our python code into SQL
class Movie(models.Model):  # Movie is a child class of Model
    rdate = models.DateField()
    moviename = models.CharField(max_length=49)
    hero = models.CharField(max_length=49)
    heroin = models.CharField(max_length=49)
    rating = models.FloatField()
# 2. python manage.py migrate  ==> it convertes our SQL code into Table(DB)

from django.db import models

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    review = models.TextField()
    hidden = models.CharField(max_length=20)
    tick = models.BooleanField(default= False)

    def __str__(self):
        return self.name

class MeroTime(models.Model):
    name = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now=True)

class Stud(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    



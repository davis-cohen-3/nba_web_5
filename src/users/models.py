from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.IntegerField()
    highscore = models.IntegerField()
    teamsCreated = models.IntegerField()
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name 

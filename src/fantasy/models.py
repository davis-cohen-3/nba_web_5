from pyexpat import model
from django.db import models

from statistics import mode
from turtle import position
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.

class fanPlayer (models.Model):
    name = models.CharField(_('Name'),max_length=255,default="")
    position = models.CharField(_('Position'),max_length=255,default="")
    age = models.FloatField(_('Age'),default=18)
    scoring_grade = models.FloatField(_('Scoring_grade'),default=0)
    passing_grade = models.FloatField(_('Passing_grade'),default=0)
    rebounding_grade = models.FloatField(_('Rebounding_grade'),default=0)
    rating = models.FloatField(_('Rating'),default=0)
    efficiency = models.FloatField(_('Efficiency'),default=0)
    turnover_grade = models.FloatField(_('Turnover_grade'),default=0)
    overall = models.FloatField(_('Overall'),default=0)
    salary = models.IntegerField(default=1000)

class team (models.Model):
    name = models.CharField(_('Name'),max_length=255,default="")
    #position = models.CharField(_('Position'),max_length=255,default="")
    age = models.FloatField(_('Age'),default=18)
    scoring_grade = models.FloatField(_('Scoring_grade'),default=0)
    passing_grade = models.FloatField(_('Passing_grade'),default=0)
    rebounding_grade = models.FloatField(_('Rebounding_grade'),default=0)
    rating = models.FloatField(_('Rating'),default=0)
    efficiency = models.FloatField(_('Efficiency'),default=0)
    turnover_grade = models.FloatField(_('Turnover_grade'),default=0)
    overall = models.FloatField(_('Overall'),default=0)
    salary = models.IntegerField(default=0)

class user_created_teams (models.Model):
    team_name = models.CharField(_('Name'),max_length=255,default="")
    mean_age = models.FloatField(default=18)
    mean_scoring = models.FloatField(default=0)
    mean_passing = models.FloatField(default=0)
    mean_rebounding = models.FloatField(default=0)
    mean_rating = models.FloatField(default=0)
    mean_efficiency = models.FloatField(default=0)
    mean_turnOver_grade = models.FloatField(default=0)
    mean_overall = models.FloatField(default=0)
    total_spendings = models.FloatField(default=0)
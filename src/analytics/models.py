from statistics import mode
from turtle import position
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Player (models.Model):

    name = models.CharField(_("FULL NAME"), max_length=255, default="")
    team = models.CharField(_("TEAM"), max_length=4, default="")
    position = models.CharField(_("POS"),max_length=4, default="")
    age = models.FloatField(_("AGE"), default=0)
    gamesPlayed = models.IntegerField(_("GP"), default=0)
    minPerGame = models.FloatField(_("MPG"), default=0)
    minPercent = models.FloatField(_("MIN%"),default=0)
    usgRate = models.FloatField(_("USG%"), default=0)
    toPercent = models.FloatField(_("TO%"), default=0)
    freethrowAtt = models.IntegerField(_("FTA"), default=0)
    ftPercent = models.FloatField(_("FT%"), default=0)
    twoPointAttempts = models.IntegerField(_("2PA"), default=0)
    twoPointPercent = models.FloatField(_("2P%"), default=0)
    threePointAttempts = models.IntegerField(_("3PA"), default=0)
    threePointPercent = models.FloatField(_("3P%"), default=0)
    fieldGoalPercent = models.FloatField(_("eFG%"), default=0)
    tsPercent = models.FloatField(_("TS%"), default=0)
    pointsPerGame = models.FloatField(_("PPG"), default=0)
    reboundsPerGame = models.FloatField(_("RPG"), default=0)
    trbPercent = models.FloatField(_("TRB%"), default=0)
    assistsPerGame = models.FloatField(_("APG"), default=0)
    assistPercent = models.FloatField(_("AST%"), default=0)
    stealPerGame = models.FloatField(_("SPG"), default=0)
    blocksPerGame = models.FloatField(_("BPG"), default=0)
    TOPerGame = models.FloatField(_("TOPG"), default=0)
    viv = models.FloatField(_("VIV"), default=0)
    offRtg = models.FloatField(_("ORTG"), default=0)
    defRtg = models.FloatField(_("DRTG"), default=0)
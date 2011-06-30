from django.db import models

class Report(models.Model):
    garden = models.CharField(max_length=140)   #'demo'
    date = models.DateTimeField('timestamp') 
    rate = models.FloatField()                  #'1.6907011032',
    #water = models.CharField(max_length=100)    #'flowing'
    water = models.IntegerField()    #'flowing'
    #tank = models.CharField(max_length=100)     #'full'
    tank = models.IntegerField()     #'full'
    #lights = models.CharField(max_length=100)   #'forward'
    lights = models.IntegerField()   #'forward'

    def __unicode__(self):
        ret = self.garden + " " + str(self.date)
        return ret 

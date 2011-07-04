from django.db import models

class Report(models.Model):
    garden = models.CharField(max_length=140)   #'demo'
    date = models.DateTimeField('timestamp') 
    arduino_uptime = models.CharField(max_length=140)   #'HH:MM:SS'
    flow_rate = models.FloatField()                  #'1.6907011032',
    flow_switch_sensor = models.IntegerField()    #flow:0
    #tank = models.CharField(max_length=100)     #'full'
    tank_level_sensor = models.IntegerField()     #full:1
    #lights = models.CharField(max_length=100)   #'forward'
    #lights = models.IntegerField()   #'forward'

    def __unicode__(self):
        ret = self.garden + " " + str(self.date)
        return ret 

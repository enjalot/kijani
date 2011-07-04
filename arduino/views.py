from django.http import HttpResponse
import json
import datetime
#from django.core import serializers


from arduino.models import Report

def index(request):
    return HttpResponse("HI")

"""
{ "report": 
    { 
    "initialize":{"initializing":0, "baudRate":38400}, 
    "arduino_uptime": "0:00:51:32", 
    "tank_level_sensor": { "full":0}, 
    "flow_switch_sensor": { "flow":1}, 
    "flow_rate_sensor": { "flowRate":1.62} 
    } 
}
"""
def upload(request):
    jsonreport = request.REQUEST["jsonreport"]
    #print jsonreport
    #example json string: 
    #http://localhost:8000/arduino/upload?jsonreport={%22garden%22:%22demo%22,%22date%22:%222011-06-18%2007:40:46%22,%22rate%22:1.6,%22water%22:1,%22tank%22:1,%22lights%22:1}
    #ss = serializers.deserialize("json", jsonreport)
    #doesn't work for now...
    #for obj in serializers.deserialize("json", jsonreport):
    #    print "obj:"
    #    print obj
    js = json.loads(jsonreport)
    jsr = js["report"]
    print jsr["flow_switch_sensor"]
    #print jsr
    #print jsono
    #this should be automated by django
    rep = Report(   #garden=js['garden'], 
                    garden="demo",
                    #date=js['date'],
                    date=datetime.datetime.now(),
                    arduino_uptime=jsr['arduino_uptime'],
                    flow_switch_sensor=jsr['flow_switch_sensor']['flow'],
                    flow_rate=jsr['flow_rate_sensor']['flowRate'],
                    tank_level_sensor=jsr['tank_level_sensor']['full'],
                    #lights=js['lights'])
                    )
    print rep
    rep.save()

    s = 'uploaded report: %s' % jsonreport
    return HttpResponse(s)


def latest(request):

    reports = """ """
    latest_reports = Report.objects.all().order_by('-date')[:5]
    for report in latest_reports:
        reports += "%s | %s | %s | %f | %d | %d <br>" % (report.garden, report.date, report.arduino_uptime, report.flow_rate, report.flow_switch_sensor, report.tank_level_sensor)#, report.lights)

    s = """
    <html><head><title>Latest Garden Reports</title></head>
    Reports: <br>
    garden | date | arduino_uptime | flow rate | flow switch sensor | tank level sensor <br>
    %(reports)s
    """ % ({'garden':"ASDF", 'reports':reports})
    return HttpResponse(s)

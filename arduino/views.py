from django.http import HttpResponse
import json
#from django.core import serializers


from arduino.models import Report

def index(request):
    return HttpResponse("HI")

def upload(request):
    jsonreport = request.REQUEST["jsonreport"]
    print jsonreport
    #example json string: 
    #http://localhost:8000/arduino/upload?jsonreport={%22garden%22:%22demo%22,%22date%22:%222011-06-18%2007:40:46%22,%22rate%22:1.6,%22water%22:1,%22tank%22:1,%22lights%22:1}
    #ss = serializers.deserialize("json", jsonreport)
    #doesn't work for now...
    #for obj in serializers.deserialize("json", jsonreport):
    #    print "obj:"
    #    print obj
    js = json.loads(jsonreport)
    #print jsono
    #this should be automated by django
    rep = Report(   garden=js['garden'], 
                    date=js['date'],
                    rate=js['rate'],
                    water=js['water'],
                    tank=js['tank'],
                    lights=js['lights'])
    print rep
    rep.save()

    s = 'uploaded report: %s' % jsonreport
    return HttpResponse(s)


def latest(request):
    garden = 'demo'

    reports = """ """
    latest_reports = Report.objects.all().order_by('-date')[:5]
    for report in latest_reports:
        reports += "%s | %d | %d | %d | %d <br>" % (report.date, report.rate, report.water, report.tank, report.lights)

    s = """
    <html><head><title>Latest Garden Reports from [ %(garden)s ]</title></head>
    Reports from %(garden)s:<br>
    %(reports)s
    """ % ({'garden':garden, 'reports':reports})
    return HttpResponse(s)

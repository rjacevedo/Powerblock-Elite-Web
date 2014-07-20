from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import *
import datetime
import json
from serializers import ReadingSerializer

@csrf_exempt
def test_response(request):
    response_data = [
        {
            'user_id': "tonyleterrible",
            'circuit_id': 123,
            'switch': {'id': 1, 'toggle': 'False'}
        },
        {
            'user_id': "futony",
            'circuit_id': 145,
            'switch': {'id': 3, 'toggle': 'True'}
        }
    ]
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def sendPD(request, login=None, circuitNum=None, value=None):
    if request.method == 'GET':
        
        now = datetime.datetime.now();

        file_object = open("PbElite/frontend.html")
        
        html = file_object.readlines()

        file_object.close()
        return HttpResponse(html)
    else:
        user = User.objects.get(login_id=login)
        rpi = RaspberryPi.objects.get(user=user.id)
        circuit = Circuit.objects.get(raspberry_pi=rpi.id, circuit_num=circuitNum)

        circuit.state = True if value=="1" else False
        circuit.save()

        response_data = {}
        response_data['result'] = value;
     
        #return HttpResponse(json.dumps(success), content_type="application/json")
        return HttpResponse(json.dumps(response_data), content_type="application/json")

def grabCircuits(request, login=None):
    if request.method == 'GET':
        user = User.objects.get(login_id=login)
        rpi = RaspberryPi.objects.get(user=user.id)
        circuits = Circuit.objects.all().filter(raspberry_pi=rpi.id)
        
        response_data = []
        
        for circuit in circuits:
            response_data.append({
                    "num": circuit.circuit_num,
                    "name": circuit.circuit_name,
                    "state": circuit.state
                })
        return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def getReading(request):
    print 'here'
    if request.method == 'POST':
        data = json.loads(request.body)
        serial = ReadingSerializer(data=data)
        print 'ahh'
        if serial.is_valid():
            serial.save()
            print 'anywhere'
            return HttpResponse(serial.data, status = 200)
        print 'failed'
        return HttpResponse(serial.errors,status = 400)


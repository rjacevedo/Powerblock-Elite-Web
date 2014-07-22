from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import *
import datetime
import json
from serializers import ReadingSerializer

@csrf_exempt
def test_response(request, login=None):
    user = User.objects.get(login_id=login)
    rpi = RaspberryPi.objects.get(user=user.id)
    circuits = Circuit.objects.all().filter(raspberry_pi=rpi.id)

    response_data = {
            'changed': False,
            'data': []
        }

    for circuit in circuits:
        print(circuit)
        if(circuit.changed == True):
            response_data['changed'] = True
            response_data['data'].append({
                    'circuit_num': circuit.circuit_num,
                    'circuit_name': circuit.circuit_name,
                    'state': circuit.state
                })
            circuit.changed = False
            circuit.save()

    response_data = {
        'changed': True,
        'data': [
            {
                'circuit_num': 1,
                'state': True
            },
            {
                'circuit_num': 2,
                'state': False
            }
        ]
    }
    
    return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def grabHomepage(request):
    if(request.method == 'GET'):
        file_object = open("PbElite/frontend.html")

        html = file_object.readlines()

        file_object.close()
        return HttpResponse(html)

@csrf_exempt
def updateCircuit(request, login=None, circuitNum=None, value=None):
    if(request.method == 'POST'):
        user = User.objects.get(login_id=login)
        rpi = RaspberryPi.objects.get(user=user.id)
        circuit = Circuit.objects.get(raspberry_pi=rpi.id, circuit_num=circuitNum)

        circuit.state = True if value=="1" else False
        circuit.changed = True
        circuit.save()

        response_data = {}
        response_data['result'] = value;
        print(value)
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
        print "hello"
        print request.body
        json_data = json.loads(request.body)
        pi = RaspberryPi.objects.get(serial_num=json_data['serial'])
        if pi != None:
            for reading in json_data['readings']:
                temp , useless= Circuit.objects.get_or_create(circuit_num=reading['circuit_num'],raspberry_pi=pi)
                reading['circuit'] = temp.id
                serial = ReadingSerializer(data=reading)
                if serial.is_valid():
                    print "valid"
                    serial.save()
                else:
                    print "invalid"
                    return HttpResponse(content="Bad Reading")
            return HttpResponse(content="OK")
        return HttpResponse(content="Specify RPi Serial Number")


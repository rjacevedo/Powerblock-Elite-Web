from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
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

def sendPD(request, value=None):
    if request.method == 'GET':
        
        now = datetime.datetime.now();

        file_object = open("PbElite/frontend.html");
        
        html = file_object.readlines();

        file_object.close();
        
        return HttpResponse(html)
    else:
        response_data = {}
        response_data['result'] = value;

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



from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import json

@csrf_exempt
def test_response(request, value=None):
    if request.method == 'GET':
        now = datetime.datetime.now()

        file_object = open("PbElite/frontend.html");
        
        html = file_object.readlines();

        file_object.close();
        return HttpResponse(html)
    else:
        response_data = {}
        response_data['result'] = 1;
        return value
        #return HttpResponse(json.dumps(response_data), content_type="application/json")

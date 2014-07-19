from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import json

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

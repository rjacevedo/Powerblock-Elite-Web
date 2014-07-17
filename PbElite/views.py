from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import json

@csrf_exempt
def test_response(request):
    if request.method == 'GET':
        now = datetime.datetime.now()
        html = "<html><body>It is now %s.</body></html>" % now
        return HttpResponse(html)
    else:
        response_data = {}
        response_data['result'] = "It worked omg!"

        return HttpResponse(json.dumps(response_data), content_type="application/json")

from django.http import HttpResponse
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from models import *
import datetime
import json
import os
import pytz
import time
from serializers import ReadingSerializer
from scheduler import createUserSchedule
import hashlib
import uuid
import re

@csrf_exempt
def test_response(request, login=None):
    print login
    user = User.objects.get(login_id=login)
    rpi = RaspberryPi.objects.get(user=user.id)
    circuits = Circuit.objects.all().filter(raspberry_pi=rpi.id)

    response_data = {
            'changed': False,
            'data': []
        }

    for circuit in circuits:
        response_data['changed'] = True
        response_data['data'].append({
                'circuit_num': circuit.id,
                'state': circuit.state
            })

    '''response_data = {
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
    }'''
    
    return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def grabLogin(request):
    if(request.method == 'GET'):
        template = loader.render_to_string("login.html")
        return HttpResponse(template)

def grabRegistration(request):
    if(request.method == 'GET'):
        template = loader.render_to_string("registration.html")
        return HttpResponse(template)

@csrf_exempt
def grabAccount(request):
    if(request.method == 'GET'):
        template = loader.render_to_string("account.html")
        return checkCookie(request,HttpResponse(template))

@csrf_exempt
def grabHomepage(request):
    """if not authenticated on any of these pages, should return login page + invalid login message"""
    if(request.method == 'GET'):
        template = loader.render_to_string("frontend.html")
        return checkCookie(request,HttpResponse(template))

def grabSchedule(request):
    if(request.method == 'GET'):
        template = loader.render_to_string("schedule.html")
        return checkCookie(request,HttpResponse(template))

@csrf_exempt
def loginRequest(request):
    if(request.method == 'POST'):
        data = request.POST;
        username = data["username"]
        password = data["password"]

        try:
            user = Login.objects.get(username=username)
        except Login.DoesNotExist:
            user = None
        
        response_data = {}
        if hasattr(user, 'password') and password == user.password:
            response_data['loginSuccess'] = 1
            rhash = os.urandom(16).encode('hex')
            usr = User.objects.get(login = user)
            expiry = datetime.datetime.now(pytz.utc) + datetime.timedelta(7,0)
            us = UserSessions(username=usr, randomhash=rhash, expiry_datetime=expiry)
            us.save()
        else:
            response_data['loginSuccess'] = 0

        return setCookieResponse(HttpResponse(json.dumps(response_data), content_type="application/json"), 'session', rhash, expiry)

@csrf_exempt
def updateCircuit(request, login=None, circuitNum=None, value=None):
    if(request.method == 'POST'):
        user = User.objects.get(login_id=login)
        rpi = RaspberryPi.objects.get(user=user.id)
        circuit = Circuit.objects.get(raspberry_pi=rpi.id, id=circuitNum)

        circuit.state = True if value=="1" else False
        circuit.changed = True
        circuit.save()

        response_data = {}
        response_data['result'] = value;
        return HttpResponse(json.dumps(response_data), content_type="application/json")

def grabCircuits(request, login=None):
    if request.method == 'GET':
        user = User.objects.get(login_id=login)
        rpi = RaspberryPi.objects.get(user=user.id)
        circuits = Circuit.objects.all().filter(raspberry_pi=rpi.id)

        response_data = []

        for circuit in circuits:
            response_data.append({
                    "num": circuit.id,
                    "name": circuit.circuit_name,
                    "state": circuit.state
                })
        return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def getReading(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        pi = RaspberryPi.objects.get(serial_num=json_data['serial'])
        if pi != None:
            for reading in json_data['readings']:
                temp , useless= Circuit.objects.get_or_create(id=reading['circuit_num'],raspberry_pi=pi)
                reading['circuit'] = temp.id
                serial = ReadingSerializer(data=reading)
                if serial.is_valid():
                    serial.save()
                else:
                    return HttpResponse(content="Bad Reading")
            return HttpResponse(content="OK")
        return HttpResponse(content="Specify RPi Serial Number")

@csrf_exempt
def grabReadings(request, login=None):
    if request.method == 'GET':
        user = User.objects.get(login_id=login)
        rpi = RaspberryPi.objects.get(user=user.id)
        circuits = Circuit.objects.all().filter(raspberry_pi=rpi.id)

        response_data = {}

        for circuit in circuits:
            reading = Reading.objects.filter(circuit_id=circuit.id).order_by("-timestamp")[:1]
            if len(reading) == 0:
                continue;
            #response_data[circuit.id] = []
            '''for reading in readings:
                response_data[circuit.id].append({
                        "reading_id": reading.id,
                        "power": reading.power,
                        "timestamp": str(reading.timestamp)
                    })'''
            response_data[circuit.id] = {
                    "name": circuit.circuit_name,
                    "power": reading[0].power,
                    "timestamp": str(reading[0].timestamp)
                }
        return HttpResponse(json.dumps(response_data), content_type="application/json")

def getUserData(request):
    data = request.GET;
    
    if data['userID'] == None : 
        return HttpResponse(content="Bad User Name")
    if request.method == 'GET' :
        user = User.objects.get(login_id = data['userID'])
        rpi = RaspberryPi.objects.get(user = data['userID'])
        response_data = {}
        response_data['firstName'] = user.first_name
        response_data['lastName'] = user.last_name
        response_data['email'] = user.email
        response_data['streetNum'] = rpi.street_num
        response_data['street_name'] = rpi.street_name
        response_data['city'] = rpi.city
        response_data['country'] = rpi.country
        response_data['postal_code'] = rpi.postal_code
        return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def updateUserData(request):
    if(request.method == 'POST'):
        data = request.POST;

        user = User.objects.get(login_id=data['userID'])
        rpi = RaspberryPi.objects.get(user=data['userID'])

        user.first_name = data['firstName'];
        user.last_name = data['lastName'];
        user.email = data['email'];
        user.save();
        
        address = data['address']
        rpi.street_num = re.sub("\D+", "", address)
        rpi.street_name = re.sub ("\d",  "", address[1:])
        rpi.city = data['city'];
        rpi.country = data['country'];
        rpi.postal_code = data['postalCode'];
        rpi.save();
        return HttpResponse()

@csrf_exempt
def postNewEvent(request):
    if request.method == 'POST':
        json_data = request.POST
        """subject to change"""
        start_time = datetime.datetime.fromtimestamp(int(json_data['start_time']))
        end_time = datetime.datetime.fromtimestamp(int(json_data['end_time']))
        print start_time
        desc = json_data['desc']
        circuit_id = json_data['circuit_id']
        onoff = json_data['onoff']
        circuit = Circuit.objects.get(pk = circuit_id)
        schedule = Schedule(start_time=start_time, end_date=end_time, description=desc, circuit=circuit,
                           state=onoff)
        schedule.save()
        createUserSchedule(schedule.pk, onoff)
        return HttpResponse(content="OK")
       
def retrieveEvents(request):
    data = request.GET
    if data['userID'] == None : 
        return HttpResponse(content="Bad User Name")
    if request.method == 'GET':
        rpi = RaspberryPi.objects.get(user = data['userID'])
        circuits = Circuit.objects.all().filter(raspberry_pi=rpi.id)

        circuitIDs = []
        for circuit in circuits:
            circuitIDs.append(circuit.id);

        events = Schedule.objects.filter(circuit__in = circuitIDs)
        
        response_data = []
        for event in events:
            response_data.append({
                    'start': time.mktime(event.start_time.timetuple()),
                    'end': time.mktime(event.end_date.timetuple()),
                    'description': event.description,
                    'circuit': event.circuit_id,
                    'state': event.state
                })

        return HttpResponse(json.dumps(response_data), content_type="application/json")

def setCookieResponse(response, key, value, expiry):
    if response == None:
        return HttpResponse(content="No Response")
    if expiry == None:
        expiry = datetime.datetime.utcnow() + datetime.timedelta(days=7)
    response.set_cookie(key, value, max_age=7*24*60*60, expires=expiry)
    return response

def checkCookie(request, response):
    """ghetto it up!"""
    template = loader.render_to_string("login.html")
    loginagain = HttpResponse(template)
    if request.COOKIES.has_key( 'session' ):
        sesh = request.COOKIES['session']
        try:
            s = UserSessions.objects.get(randomhash = sesh)
            if datetime.datetime.now(pytz.utc) > s.expiry_datetime:
                s.delete()
            else:
                return response
        except UserSessions.DoesNotExist:

            return loginagain
    return loginagain

@csrf_exempt
def logout (request):
    if request.COOKIES.has_key('session'):
        sesh = request.COOKIES['session']
        s = UserSessions.objects.get(randomhash=sesh)
        s.delete()
        return HttpResponse(content='OK')

@csrf_exempt
def getChartData(request):
    if request.method == 'POST':
        data = request.POST
        c = Circuit.objects.get(pk=data['circuit_num'])
        earlystamp = datetime.datetime.now(pytz.utc) - datetime.timedelta(days=30)
        readings = Reading.objects.all().filter(circuit=c, timestamp__gte=earlystamp).order_by('timestamp')
        readingsArr = []
        for r in readings:
            readingsArr.append({'timestamp': time.mktime(r.timestamp.timetuple())*1000, 'reading': r.power})
        response_data = {}
        response_data['circuit_name'] = c.circuit_name
        response_data['readings'] = readingsArr
        return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def registerUser(request):
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        password = data['password']
        rpid = data['registrationKey']
        salt = uuid.uuid4().hex
        hashed_password = hashlib.sha512(password + salt).hexdigest()
        try:
            login = Login.objects.get(username=username)
            return HttpResponse(content='Duplicate User Name')
        except Login.DoesNotExist:
            login = Login(username = username, password = hashed_password, salt = salt)
            login.save()
            user = User(login = login, first_name = data['firstname'], last_name = data['lastname'], email = data['email'])
            user.save()
            address = data['address']
            try:
                rpi = RaspberryPi.objects.get(pk = rpid)
                return HttpResponse(content= 'Duplicate RPID')
            except RaspberryPi.DoesNotExist:
                rpi = RaspberryPi(
                    serial_num = rpid,
                    user = user,
                    model = 'Powerblock Elite v1',
                    city = data['city'],
                    country = data['country'],
                    street_num = re.sub("\D+", "", address),
                    street_name = re.sub ("\d",  "", address[1:]),
                    postal_code = data['postalCode']
                )
                return HttpResponse(content='OK')
        
@csrf_exempt
def deleteSchedule(request)
    if request.method == 'POST':
        data = request.POST
        schedule_id = data['scheduleID']
        try:
            schedule = Schedule.objects.get(pk = schedule_id)
            schedule.delete()
            return HttpResponse(content='OK')
        except Schedule.DoesNotExist:
            return HttpResponse(content='Bad Schedule ID')















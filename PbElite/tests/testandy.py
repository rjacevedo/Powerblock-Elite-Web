import urllib2
import json
import datetime
import random
random.seed(0)
data = {}
data['serial']='rpijavier'
data['readings']=[]
readings = data['readings']
readings.append({'circuit_num':1,'voltage':random.random(),'current':random.random()})
data = json.dumps(data)
print data
url = 'http://127.0.0.1:8000/api/sendReading'
a = urllib2.urlopen(url, data)
print a.read()

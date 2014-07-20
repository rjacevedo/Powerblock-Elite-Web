import urllib2
import json
import datetime

data = json.dumps({'circuit':1,'voltage':2, 'current':3})
print data
url = 'http://127.0.0.1:8000/api/sendReading'
print urllib2.urlopen(url, data)

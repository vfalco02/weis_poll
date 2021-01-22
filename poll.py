import sys
import urllib.request

resp = urllib.request.urlopen('https://c.ateb.com/3f647956b456425d9c12360db8e4fdb4/')

body = resp.read().decode('utf-8')

if 'Appointments Full' in body:
  sys.exit(1)
  
sys.exit(0)

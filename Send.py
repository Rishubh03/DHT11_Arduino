import serial
import time
import urllib.request

ser=serial.Serial('COM3',9600,timeout=1)
while True:
  b=ser.readline()
  b=b.decode()
  if len(b)>0:
    humidity=b[0:2]
    temperature=b[6:8]
    urllib.request.urlopen("https://api.thingspeak.com/update?api_key=E4OGI5JK4R6R0ONQ&field1="+str(humidity))
    urllib.request.urlopen("https://api.thingspeak.com/update?api_key=E4OGI5JK4R6R0ONQ&field2="+str(temperature))

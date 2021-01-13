#prctice
#Importing URL, Json, SSL Libraries 
import urllib.request, urllib.parse, urllib.error
import json
import ssl

#Assinging API Key false, If you have API key use it 
api_key = False

#if you dont have API key it will go to already collected data in the URL, or it will go to google maps to collect the data ffrom google API  
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

#SSL Certificate error code, to enter into secured Website
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#looping to get data of each address
while True:
    address = input('Enter location: ')
#sanity check
    if len(address) < 1:break
#creating Complete URL with address
    url = serurl + urllib.parse.urlopen({'address' : address})

    print('retrieving', url)
#Opening the URL 
    ur = urllib.request.urlopen(url)
#Reading and Decodeing the data  
    data =ur.read().decode()
#try to load data if it fails return None
    try:
        js = json.loads(data)
    except:
        js = None
#checking the status of the address avilable
        if not js or 'status' not in js or js['status'] !='ok':
            print('failed')
            print(data)
            continue
#Printing Lattitude and Longitude 
        lat = js["results"][0]["geomentry"]["location"]["lat"]
        lng = js["results"][0]["geomentry"]["location"]["lng"]
        print('lat', lat, 'lng', lng)
#Printing the address
        location = js["results"][0]['formatted_address']
        print(location)

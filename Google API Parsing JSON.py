#prctice
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


while True:
    address = input('Enter location: ')
    if len(address) < 1:break
    url = serurl + urllib.parse.urlopen({'address' : address})

    print('retrieving', url)
    ur = urllib.request.urlopen(url)
    data =ur.read().decode()

    try:
        js = json.loads(data)
    except:
        js = None

        if not js or 'status' not in js or js['status'] !='ok':
            print('failed')
            print(data)
            continue
        lat = js["results"][0]["geomentry"]["location"]["lat"]
        lng = js["results"][0]["geomentry"]["location"]["lng"]
        print('lat', lat, 'lng', lng)
        location = js["results"][0]['formatted_address']
        print(location)

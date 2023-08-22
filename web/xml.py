import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro
# http://py4e-data.dr-chuck.net/comments_1762266.xml

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/comments_1762266.xml'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'


while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    # parms = dict()
    # parms['address'] = address
    
    # if api_key is not False: parms['key'] = api_key
    
    # url = serviceurl + urllib.parse.urlencode(parms)
    
    print('Retrieving', address)
    
    res = urllib.request.urlopen(address)

    data = res.read()
    # print('Retrieved', len(data), 'characters')
    # print(data.decode())
    
    # XML Tree Fromation for Traversal
    tree = ET.fromstring(data)
    print(dir(tree))
    
    sum = 0
    results = tree.findall(".//count")
    print(results)
    for result in results:
        print(result.text)
        sum = sum + int(result.text)
    
    print(sum)
    # lat = results[0].find('geometry').find('location').find('lat').text
    # lng = results[0].find('geometry').find('location').find('lng').text
    # location = results[0].find('formatted_address').text

    # print('lat', lat, 'lng', lng)
    # print(location)
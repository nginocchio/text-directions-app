import urllib.parse
import urllib.request
import json

def gather_locations():
    list_of_user_addresses = []
    trip_locations = input().split()
    while len(trip_locations) != 1 or not trip_locations[0].isdigit() or int(trip_locations[0]) < 2:
        trip_locations = input().split()
    for i in range(int(trip_locations[0])):
        address = input()
        list_of_user_addresses.append(address)
    return list_of_user_addresses



def gather_stats():
    list_of_info = []
    trip_stats = input().split()
    while len(trip_stats) != 1 or not trip_stats[0].isdigit() or trip_stats[0] not in '12345' :
        trip_stats = input().split()
    for j in range(int(trip_stats[0])):
        info = input()
        list_of_info.append(info)

    return list_of_info



def create_tuples(list_of_locations):
    '''returns a list of tuples'''
    locations = list_of_locations
    new_tuple = []
    new_tuple.append(('from', locations[0]))
    for i in range(1, len(locations[1:]) + 1):
        new_tuple.append(())
        new_tuple[i] = new_tuple[i] + ('to', locations[i])

    return new_tuple


def url_encode(list_of_tuples):
    '''returns a str representation of a URL-encoded query'''
    return urllib.parse.urlencode(list_of_tuples)


def http_response(url_encoded_query):
    '''takes in a encoded URL, and returns full http response '''
    half_url = 'http://open.mapquestapi.com/directions/v2/route?key=GyBs1GX0eUhSwuSGRAEb54dFb7tlQ6Or&'
    full_url = half_url + url_encoded_query
    #print(full_url)
    response = urllib.request.urlopen(full_url)
    return response





def parse_the_response(response):
    '''converts response to a string and returns the json object as a dictionary '''
    data = response.read()
    response.close()
    text = data.decode(encoding='utf-8')
    obj = json.loads(text)
    return obj





def elevation_full_url(list_of_lat_and_long):
    full_url = 'http://open.mapquestapi.com/elevation/v1/profile?key=GyBs1GX0eUhSwuSGRAEb54dFb7tlQ6Or&shapeFormat=raw&latLngCollection='
    for num in list_of_lat_and_long:
        full_url += str(num) + ','
    response = urllib.request.urlopen(full_url[:-1])
    return parse_the_response(response)











import json
from math import sin, cos, radians, acos

def findDistanceFromOffice(latitude, longitude):
    dublinRadiansLatitude = radians(float(53.339428))
    dublinRadiansLongitude = radians(float(-6.257664))
    personRadiansLatitude = radians(float(latitude))
    personRadiansLongitude = radians(float(longitude))
    radiusOfEarth = 6371

    dist = radiusOfEarth * acos(sin(dublinRadiansLatitude)*sin(personRadiansLatitude) + cos(dublinRadiansLatitude)*cos(personRadiansLatitude)*cos(dublinRadiansLongitude - personRadiansLongitude))
    return dist

def main():
    with open('customers.txt') as file:
        line = file.readline()
        while line:
            j = json.loads(line)
            dist = findDistanceFromOffice(j['latitude'], j['longitude'])
            print dist
            line = file.readline()

if __name__ == "__main__": main()

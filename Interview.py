import sys
import json
import os.path
from math import sin, cos, radians, acos

class Interview:
    def findDistanceFromOffice(self, latitude, longitude):
        dublinRadiansLatitude = radians(float(53.339428))
        dublinRadiansLongitude = radians(float(-6.257664))
        personRadiansLatitude = radians(float(latitude))
        personRadiansLongitude = radians(float(longitude))
        radiusOfEarth = 6371

        dist = radiusOfEarth * acos(sin(dublinRadiansLatitude)*sin(personRadiansLatitude) + cos(dublinRadiansLatitude)*cos(personRadiansLatitude)*cos(dublinRadiansLongitude - personRadiansLongitude))
        return dist

    def readFile(self, fileName):
        dictionary = []
        with open(fileName) as file:
            line = file.readline()
            while line:
                j = json.loads(line)
                dist = self.findDistanceFromOffice(j['latitude'], j['longitude'])
                if(dist < 100):
                    dictionary.append([j['user_id'], dist])
                line = file.readline()
        dictionary.sort(key=lambda x: x[0])
        return dictionary

    def process(self, file):
        if os.path.exists(file):
            dictionary = self.readFile(file)
            print 'user_id', ' ', 'distance'
            for user_id, distance in dictionary:
                print user_id, '       ', distance
        else:
            print 'Bad File name'

def main():
    interview = Interview();
    interview.process(sys.argv[1])


if __name__ == "__main__": main()

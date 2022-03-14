
class cartesianCordinate:
    def __init__(self,x=0.,y=0.,z=0.):
        self.x = x
        self.y = y
        self.z = z
    def setxyz(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def toRadialCord(self):
        pass#todo
    def dot(self,cord):
        pass#todo
    def cross(self):
        pass#todo

class radialCordinate:
    def __init__(self,lon=0,lat=0,alt=0):
        self.lon = lon
        self.lat = lat
        self.alt = alt
    def setLonLatAlt(self,lon,lat,alt):
        self.lon = lon
        self.lat = lat
        self.alt = alt
    def toCartesianCord(self):
        pass#todo

class radialVelocity:
    def __init__(self,angleFromEast=0.,angleFromLevel=0.,speed=1):
        self.horizontalInclination = angleFromEast
        self.verticalinclination = angleFromLevel
        self.speed = speed

print("FooBarBaz")
import math

class vector3:
    def __init__(self,x=0.,y=0.,z=0.):
        self.x = x
        self.y = y
        self.z = z
    def setxyz(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def toRadial(self):
        r = self.magnitude()
        lon = math.atan2(self.y,self.x)
        lat = math.asin(self.z/r)
        return radialCordinate(lon,lat,r)
    def magnitude(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) * 0.5
    def dot(self,v):
        return self.x*v.x+self.y*v.y+self.z+v.z
    def cross(self,v):
        x = self.y*v.z - self.z*v.y
        y = self.z*v.x - self.x*v.z
        z = self.x*v.y - self.y*v.x
        return vector3(x,y,z)

def radians(degrees):
    return math.pi*degrees/180.

def degrees(radians):
    return 180.*radians/math.pi

class radialCordinate:
    def __init__(self,lon=0,lat=0,radius=0):
        self.lon = lon
        self.lat = lat
        self.radius = radius
    def asDegrees(self):
        return f"Longitude:{degrees(self.lon)}\nLatitude:{degrees(self.lat)}\nRadius:{self.radius}"
    def setLonLatAlt(self,lon,lat,alt):
        self.lon = lon
        self.lat = lat
        self.radius = alt + 6378.137 # altitude + earth's approximate radius
    def toCartesian(self):
        x = self.radius * math.cos(self.lon) * math.cos(self.lat)
        y = self.radius * math.sin(self.lon) * math.cos(self.lat)
        z = self.radius * math.sin(self.lat)
        return vector3(x,y,z)

class parentBody:
    def __init__(self,
                 satellites = [],
                 year = 365.25*24*60*60 ,
                 day = 24*60*60 ,
                 mass = 5.9722 * 10**24 ,
                 inclination = degrees(23.5)
                 ):
        self.satellites = satellites
        self.year = year
        self.day = day
        self.mass = mass
        self.inclination = inclination
    # todo

class satellite: # radians kilometers and kilometers per second.
    def __init__(self,position = radialCordinate(0,0,2000),velocity = vector3(0,0,8)):
        if type(position) == vector3:
            self.position = position.toRadial()
        elif type(position) == radialCordinate:
            self.position = position
        else:
            raise TypeError
        if type(velocity) == vector3:
            self.velocity = velocity
        elif type(velocity) == radialCordinate:
            raise TypeError
            # todo get from position and observed velocity to velocity vector
        self.orbitalPlane = self.position.toCartesian().cross(self.velocity)

print("FooBarBaz")
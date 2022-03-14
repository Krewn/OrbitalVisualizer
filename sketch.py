import spacialutils
import time
import threeJS

class satellite:
    def init(self,radialCord,radialVelocity):
        self.t0 = time.time()
        self.p0 = radialCord
        self.v0 = radialVelocity

class centeralBody:
    def init(self):
        self.satellites = []
    def draw(self):
        pass  # todo

s = threeJS.scene()
s.output()



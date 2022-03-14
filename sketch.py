import spacialutils as spu
import time
import threeJS

spu.parentBody(spu.satellite())
s = threeJS.scene()
s.output()

scene = threeJS.scene()
scene.add(threeJS.sphere())
scene.add(threeJS.sphere(spu.vector3(1.5,0,0),size=0.1,name="satellite"))
scene.output()


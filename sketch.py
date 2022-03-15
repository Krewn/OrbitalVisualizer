import spacialutils as spu
import time
import threeJS

spu.parentBody(spu.satellite())
s = threeJS.scene()
s.output()

scene = threeJS.scene()
earth = threeJS.sphere()

satellite = threeJS.sphere(spu.vector3(1.5,0,0),size=0.1,name="satellite")
satellite.motion = f"""function(t){"{"}this.mesh.position.set(Math.sin(t)*1.5,Math.cos(t)*1.5,0);{"}"}"""

scene.add(earth)
scene.add(satellite)
scene.output()


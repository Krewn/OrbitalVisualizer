import spacialutils as spu

class sphere:
    def __init__(self,position=spu.vector3(0,0,0),size=1,name="earth"):
        self.position = position
        self.size = size
        self.name = name
    def script(self):
        return f"""
        var {self.name}_geometry = new THREE.SphereGeometry({self.size}, 32, 32);
        var {self.name}_material = new THREE.MeshPhongMaterial();
        var {self.name}_mesh = new THREE.Mesh({self.name}_geometry, {self.name}_material);
        {self.name}_mesh.position.set({self.position.x},{self.position.y},{self.position.z});
        //{self.name}_material.map = THREE.ImageUtils.loadTexture('../earth.jpg');
        scene.add({self.name}_mesh);
        """

class conicSection:
    def __init__(self,normalVector = spu.vector3(0,0,1)):
        self.plane = normalVector
        pass #todo

class scene:
    def __init__(self):
        self.objects=[]
    def add(self,object):
        self.objects.append(object)
    def output(self,destination = "threeJSPlot.html"):
        doc = """
        <!DOCTYPE html>
        <html>
        <head>
        <title>Page Title</title>
        </head>
        <body>
        
        <h1>FooBarBaz</h1>
        <p>LaDeDa</p>
        <script src=../three.min.js></script>
        <script>"""+self.script()+"""</script>
        </body>
        </html>
        """
        with open(destination,"w") as f:
            f.write(doc)
        return(doc)
    def script(self):
        return """var scene = new THREE.Scene();
        var camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );

        var renderer = new THREE.WebGLRenderer();
        renderer.setSize( window.innerWidth, window.innerHeight );
        document.body.appendChild( renderer.domElement );

        """+"\n".join([object.script() for object in self.objects])+"""
        
        var light = new THREE.HemisphereLight(0xf6e86d, 0x404040, 0.5);
        scene.add(light);
        
        camera.position.x = 0;
        camera.position.y = -5;
        camera.position.z = 0;
        camera.lookAt(new THREE.Vector3( 0, 0, 0));
        
        var render = function () {
            requestAnimationFrame( render );
            renderer.render(scene, camera);
        }

        //Create an render loop to allow animation
        /*var render = function () {
            requestAnimationFrame( render );

            cube.rotation.x += 0.1;
            cube.rotation.y += 0.1;

            renderer.render(scene, camera);
        };*/

        render();
        """




import spacialutils as spu

class sphere:
    def __init__(self,position=spu.vector3(0,0,0),size=1,name="earth",motion="function(t){return}"):
        self.position = position
        self.size = size
        self.name = name
        self.motion = motion
    def script(self):
        return f"""
            {"{"}
                name : "{self.name}",
                mesh : new THREE.Mesh(new THREE.SphereGeometry({self.size}, 32, 32), new THREE.MeshPhongMaterial()),
                init : function(scene){"{"}
                this.mesh.position.set({self.position.x},{self.position.y},{self.position.z});
                //this.material.map = THREE.ImageUtils.loadTexture('../earth.jpg');
                scene.add(this.mesh);
                {"}"},
                animate : {self.motion}
            {"}"}"""

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
        </script><script src=../three.min.js></script>
        </script><script src=../TrackballControls.js></script>
        <!-- 
        <script src="http://threejs.org/build/three.min.js"></script>
        <script src="https://threejs.org/examples/js/controls/TrackballControls.js"></script> 
        -->
        <script>"""+self.script()+"""</script>
        </body>
        </html>
        """
        with open(destination,"w") as f:
            f.write(doc)
        return(doc)
    def script(self):
        return """
        var scene = new THREE.Scene();
        var camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );
        
        var renderer = new THREE.WebGLRenderer();
        renderer.setSize( window.innerWidth, window.innerHeight );
        
        var objects = ["""+",".join([object.script() for object in self.objects])+"""];
        objects.forEach(object => object.init(scene));
        
        var light = new THREE.HemisphereLight(0xf6e86d, 0x404040, 0.5);
        scene.add(light);
        
        camera.position.x = 0;
        camera.position.y = -5;
        camera.position.z = 0;
        camera.lookAt(new THREE.Vector3( 0, 0, 0));
        var timeStep = 0.01;
        var time = 0;
        var controls = new THREE.TrackballControls( camera, renderer.domElement );
        controls.target.set( 0, 0, 0 ); // Zoom works rotation does not.
        var renderOnce = function () {
            time += timeStep;
            objects.forEach(object => object.animate(time));
            controls.update();
            renderer.render(scene, camera);
        }
        var render = function () {
            renderOnce();
            requestAnimationFrame( render );
        }
        window.addEventListener('resize', onWindowResize, false)
        function onWindowResize() {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderOnce();
        }
        
        document.body.appendChild( renderer.domElement );
        render();"""




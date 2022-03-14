import spacialutils as s

class sphere:
    def __init__(self,position=s.cartesianCordinate(0,0,0),size=1):
        self.position = position
        self.size = 0
    def script(self):
        pass#todo

class conicSection:
    def __init__(self):
        pass #todo

class scene:
    def init(self):
        self.objs=[]
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

        var geometry = new THREE.BoxGeometry( 1, 1, 1 );
        var material = new THREE.MeshLambertMaterial( { color: 0x00ff00 } );
        var cube = new THREE.Mesh( geometry, material );
        scene.add( cube );
        
        var light = new THREE.HemisphereLight(0xf6e86d, 0x404040, 0.5);
        scene.add(light);
        
        camera.position.z = 5;

        //Create an render loop to allow animation
        var render = function () {
            requestAnimationFrame( render );

            cube.rotation.x += 0.1;
            cube.rotation.y += 0.1;

            renderer.render(scene, camera);
        };

        render();
        """




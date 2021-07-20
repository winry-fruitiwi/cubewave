# Cube wave by BeesAndBombs, demonstrated by Daniel Shiffman
# v0.1 - shell, code and version comments
# v0.2 - 2D cube wave with varying opacity, like panes shifting to reflect sunlight
# v0.3 - 3D cube wave
# v0.4 - addition. Plans: flashing rectangles moving like a jellyfish with movement functionality!
add_library("peasycam") # we just want to be able to rotate the jellyfish

def setup():
    global w
    w = 10
    # square(0, 0, 10) # this is just a test
    colorMode(HSB, 360, 100, 100, 100)
    size(600, 600, P3D)
    background(220, 79, 35)
    cam = PeasyCam(this, width/2, height/2, 0, 500)


def draw():
    global w
    translate(width/2, height/2)
    background(220, 79, 35)
    # we want there to be a grid filled with squares of low alpha.
    #
        #
    # let's make our first square!
    pushMatrix()
    # I'll translate so we don't have to input positions
    # translate(x, y, 0)
    fill(0, 0, 100, 10)
    square(0, 0, w)
            
            
    popMatrix()

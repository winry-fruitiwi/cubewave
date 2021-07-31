# Cube wave by BeesAndBombs, demonstrated by Daniel Shiffman from The Coding Train
# v0.1 - shell, code and version comments
# v0.2 - 2D cube wave with varying opacity, like panes shifting to reflect sunlight
# v0.3 - 3D cube wave
# v0.4 - addition. Plans: flashing rectangles moving like a jellyfish with movement functionality!
add_library("peasycam") # we just want to be able to rotate the jellyfish

def setup():
    global w, angle
    angle = 0
    w = 50
    # square(0, 0, 10) # this is just a test
    rectMode(CENTER)
    colorMode(HSB, 360, 100, 100, 100)
    size(600, 600, P3D)
    background(220, 79, 35)
    cam = PeasyCam(this, width/2, height/2, 0, 500)
    noStroke()


def draw():
    global w, angle
    background(220, 79, 35)
    translate(width/2, height/2)
    
    # we want there to be a grid filled with squares of low alpha.
    # The end result for 2D should be a grid of squares with varying opacity to simulate a sine wave.
    # The end result for plain 3D should be a grid of boxes that oscillate.
    # The end result for modified 3D should be a jellyfish-like structure that flashes in the dark.
    # Like last time I will see if I can implement movement controls.
    for x in range(-width, width + w, w):
        for y in range(-height, height + w, w):
            # let's make our first square!
            pushMatrix()
            
            # I'll translate so we don't have to input positions.
            translate(x, y, 0)
            
            # the general sine formula is a*sin(b(x+c)) + d. We only care about b so we get sin(b(x)).
            # b * p = 2pi. In this case, p = width, so b = 2pi/width.
            distance = sqrt(x*x + y*y)
            h = sin(2*PI/width * (distance + angle))
            
            # map the alpha of each square to the sine function's range.
            a = map(h, -1, 1, 10, 80)
            # we want to do the same thing for h (height), only it's a larger range.
            h = map(h, -1, 1, 100, 800)
            # Make the rectangles. Change to boxes in plain 3D and, in this case, rectangles in modded 3D.
            # when using boxes, the alpha fill will make things too bright.
            fill(0, 0, 100, 10)
            # rect is for 2D, box is for 3D. Use either the alpha or the height h variable.
            # rect(0, 0, w, w)
            box(w, w, h)
            popMatrix()
    
    angle += 2

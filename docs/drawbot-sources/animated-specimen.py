# Render this specimen GIF with DrawBot3: http://www.drawbot.com/
import math
import os

# Basic variables:
W, H, M = 1024, 1024, 128

# Grid drawn from a given increment:
def grid(inc):
    stroke(0.6, 0, 0)  # Set grid line color
    stpX, stpY = 0, 0  # Step in sequence on x axis
    incX, incY = inc, inc  # Grid increment
    for x in range(int(((W-(M*2))/inc)+1)):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX  # Set position for next gridline
    for y in range(int(((H-(M*2))/inc)+1)):
        polygon((M, M+stpY), (H-M, M+stpY))
        stpY += incY  # Set position for next gridline



newPage(W, H)
fill(0)           # Background color
rect(0, 0, W, H)  # Draw the background

# Draw the grid (uncomment next line)
grid(32)

# Basic Style
stroke(None)
fill(1)

rect(100, 100, 100, 100)

# Save GIF
#saveImage("animated-specimen.gif")


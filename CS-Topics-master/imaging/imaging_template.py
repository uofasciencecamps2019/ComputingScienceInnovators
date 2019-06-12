#!/usr/bin/env python3

"""
The name of your file
Your first and last name

Description of your file

A link to any external sources you use
*** looking online for help is fine, just make sure you provide a link to the websites you used ***
"""

# ============================================================================
# Image processing with cImage
# ============================================================================
# Pixel Methods
# - Pixel(r, g, b)  --  creates a pixel object
# - getRed()        -- returns pixel intensity, like getGreen() and getBlue()
# - setRed(r)       -- sets pixel intensiry, like setBlue(b) and setGreen(g)
#
# Image Window Methods
# - ImageWin(t, w, h)   -- creates a window with t title, w width, h height
# - getMouse()          -- returns position of the mouse click
# - exitOnClick()       -- closes the image window
#
# Image Methods
# - EmptyImage(w, h)    --  creates empty image object with w width, h height
# - FileImage(f)        --  creates an image object from f file
# - draw(win)           --  draws the image in win window
# - save(f)             --  saves the image to f file
# - getWidth()          --  self explanatory
# - getHeight()         --  self explanatory
# - getPixel(c, r)      --  self explanatory
# - setPixel(c, r, p)   --  self explanatory (p pixel)
# - setPosition(c, r)   --  self explanatory
# ============================================================================

from cImage import *

# WARNING: Don't touch this function, it is to be left as it is
def main():
	functions = [make_blue, negative_pixel, grayscale]
	
	filename = input("Enter filename")
	imgWindow = ImageWin("IP", 500, 500)
	oldImage = FileImage(old)
	
	width = oldImage.getWidth()
	height = oldImage.getHeight()
	newImage = EmptyImage(width, height)

	for f in functions:
		for row in range(height):
			for col in range(width):
				originalPixel = oldImage.getPixel(col, row)
				newPixel = f(originalPixel)
				newImage.setPixel(col, row, newPixel)
			newImage.setPosition(width + 1, 0)
			newImage.draw(imgWindow)
			imgWindow.exitOnClick()
	
	
# Taking a pixel and making it completely blue
def make_blue(old_pixel):
	# Code here
  
  
# Constructing a negative pixel (negative = 255 - original)
def negative_pixel(new_pixel):
	# Code here


# Construct a grayscale pixel (Each RGB value is the average of the original pixel's red, green, and blue value)
def grayscale(old_pixel):
	# Code here
	

if __name__ == "__main__":
	main()

"""
File: fire.py
Name: Doris
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def main():
    """
    This program highlights wildfire areas as red in a grayscale version of the original image.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


def highlight_fires(filename):
    """
    :param filename: str, the file path of the original image (with respect to current directory)
    :return highlighted_img: SimpleImage, an image with wildfire areas marked in red and the rest in gray
    """
    highlighted_img = SimpleImage(filename)
    for pixel in highlighted_img:
        avg = (pixel.red + pixel.green + pixel.blue)//3
        if pixel.red > avg*HURDLE_FACTOR:
            # Wildfire area
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return highlighted_img


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

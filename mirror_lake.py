"""
File: mirror_lake.py
Name: Doris
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def main():
    """
    This program creates a mirrored image by placing an inverted original image below the original one.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


def reflect(filename):
    """
    :param filename: str, the file path of the original image (with respect to current directory)
    :return b_img: SimpleImage, the mirrored image
    """
    r_img = SimpleImage(filename)
    b_img = SimpleImage.blank(r_img.width, r_img.height * 2)  # Create a blank canvas
    for x in range(r_img.width):
        for y in range(r_img.height):
            # Colored Pixel
            r_img_pixel = r_img.get_pixel(x, y)

            # Blank Pixel on the upper side
            b_img_pixel1 = b_img.get_pixel(x, y)
            b_img_pixel1.red = r_img_pixel.red
            b_img_pixel1.green = r_img_pixel.green
            b_img_pixel1.blue = r_img_pixel.blue

            # Blank Pixel on the downward side
            b_img_pixel2 = b_img.get_pixel(x, b_img.height - 1 - y)
            b_img_pixel2.red = r_img_pixel.red
            b_img_pixel2.green = r_img_pixel.green
            b_img_pixel2.blue = r_img_pixel.blue
    return b_img


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

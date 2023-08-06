"""
File: flip_horizontally.py
Name: Doris
------------------------------------
This program shows how to create an empty SimpleImage
as well as making a mirrored image of poppy.png by
replacing pixels on blank new canvas by ones on poppy.png
"""


from simpleimage import SimpleImage


def main():
    img = SimpleImage("images/poppy.png")
    img.show()

    # Create a blank canvas
    b_img = SimpleImage.blank(img.width*2, img.height)
    b_img.show()

    for x in range(img.width):
        for y in range(img.height):
            # Colored Pixel
            img_pixel = img.get_pixel(x, y)

            # Blank Pixel on the left side
            b_img_pixel1 = b_img.get_pixel(x, y)
            b_img_pixel1.red = img_pixel.red
            b_img_pixel1.green = img_pixel.green
            b_img_pixel1.blue = img_pixel.blue

            # Blank Pixel on the right side
            b_img_pixel2 = b_img.get_pixel(b_img.width-1-x, y)
            b_img_pixel2.red = img_pixel.red
            b_img_pixel2.green = img_pixel.green
            b_img_pixel2.blue = img_pixel.blue
    b_img.show()
    

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()

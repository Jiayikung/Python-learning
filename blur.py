"""
File: blur.py
Name: Doris
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def main():
    """
    This program creates a blurred image that uses the average RGB values of a pixel's nearest neighbors.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):  # Assume we blurred the image five times
        blurred_img = blur(blurred_img)
    blurred_img.show()


def blur(img):
    """
    :param img: SimpleImage, the original image
    :return new_img: SimpleImage, the blurred image
    """
    # Create a new blank img that is as big as the original one
    new_img = SimpleImage.blank(img.width, img.height)

    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x, y)
            new_img_pixel = new_img.get_pixel(x, y)
            red1 = 0  # The sum of red bytes from designated pixels
            green1 = 0  # The sum of green bytes from designated pixels
            blue1 = 0  # The sum of blue bytes from designated pixels

            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.
                for p in range(2):
                    for q in range(2):
                        img_pixel = img.get_pixel(p, q)
                        red1 += img_pixel.red
                        green1 += img_pixel.green
                        blue1 += img_pixel.blue
                new_img_pixel.red = red1//4
                new_img_pixel.green = green1//4
                new_img_pixel.blue = blue1//4

            elif x == img.width-1 and y == 0:
                # Get pixel at the top-right corner of the image.
                for p in range(img.width-2, img.width):
                    for q in range(2):
                        img_pixel = img.get_pixel(p, q)
                        red1 += img_pixel.red
                        green1 += img_pixel.green
                        blue1 += img_pixel.blue
                new_img_pixel.red = red1//4
                new_img_pixel.green = green1//4
                new_img_pixel.blue = blue1//4

            elif x == 0 and y == img.height-1:
                # Get pixel at the bottom-left corner of the image
                for p in range(2):
                    for q in range(img.height-2, img.height):
                        img_pixel = img.get_pixel(p, q)
                        red1 += img_pixel.red
                        green1 += img_pixel.green
                        blue1 += img_pixel.blue
                new_img_pixel.red = red1//4
                new_img_pixel.green = green1//4
                new_img_pixel.blue = blue1//4

            elif x == img.width-1 and y == img.height-1:
                # Get pixel at the bottom-right corner of the image
                for p in range(img.width-2, img.width):
                    for q in range(img.height-2, img.height):
                        img_pixel = img.get_pixel(p, q)
                        red1 += img_pixel.red
                        green1 += img_pixel.green
                        blue1 += img_pixel.blue
                new_img_pixel.red = red1//4
                new_img_pixel.green = green1//4
                new_img_pixel.blue = blue1//4
 
            elif 0 < x < img.width-1 and y == 0:
                # Get top edge's pixels (without two corners)
                for p in range(x-1, x+2):
                    for q in range(2):
                        img_pixel = img.get_pixel(p, q)
                        red1 += img_pixel.red
                        green1 += img_pixel.green
                        blue1 += img_pixel.blue
                new_img_pixel.red = red1//6
                new_img_pixel.green = green1//6
                new_img_pixel.blue = blue1//6

            elif 0 < x < img.width-1 and y == img.height-1:
                # Get bottom edge's pixels (without two corners)
                for p in range(x-1, x+2):
                    for q in range(img.height-2, img.height):
                        img_pixel = img.get_pixel(p, q)
                        red1 += img_pixel.red
                        green1 += img_pixel.green
                        blue1 += img_pixel.blue
                new_img_pixel.red = red1 // 6
                new_img_pixel.green = green1 // 6
                new_img_pixel.blue = blue1 // 6

            elif x == 0 and 0 < y < img.height-1:
                # Get left edge's pixels (without two corners)
                for p in range(2):
                    for q in range(y-1, y+2):
                        img_pixel = img.get_pixel(p, q)
                        red1 += img_pixel.red
                        green1 += img_pixel.green
                        blue1 += img_pixel.blue
                new_img_pixel.red = red1 // 6
                new_img_pixel.green = green1 // 6
                new_img_pixel.blue = blue1 // 6

            elif x == img.width-1 and 0 < y < img.height-1:
                # Get right edge's pixels (without two corners)
                for p in range(img.width-2, img.width):
                    for q in range(y-1, y+2):
                        img_pixel = img.get_pixel(p, q)
                        red1 += img_pixel.red
                        green1 += img_pixel.green
                        blue1 += img_pixel.blue
                new_img_pixel.red = red1 // 6
                new_img_pixel.green = green1 // 6
                new_img_pixel.blue = blue1 // 6

            else:
                # Inner pixels.
                for p in range(x-1, x+2):
                    for q in range(y-1, y+2):
                        img_pixel = img.get_pixel(p, q)
                        red1 += img_pixel.red
                        green1 += img_pixel.green
                        blue1 += img_pixel.blue
                new_img_pixel.red = red1 // 9
                new_img_pixel.green = green1 // 9
                new_img_pixel.blue = blue1 // 9

    return new_img



if __name__ == '__main__':
    main()

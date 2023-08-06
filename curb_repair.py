"""
File: curb_repair.py
Name: Doris
-------------------------------
This program shows how to detect red pixels
of curb and change them into gray scale, making
the curb area be considered as an available parking space!
"""


from simpleimage import SimpleImage

THRESHOLD = 1.123


def main():
    img = SimpleImage("images/curb.png")
    for pixel in img:
        avg = (pixel.red + pixel.green + pixel.blue)//3
        if pixel.red > avg*THRESHOLD:
            # Gray
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    img.show()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()

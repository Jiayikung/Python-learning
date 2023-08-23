"""
File: my_drawing.py
Name: Doris
----------------------
This file uses the campy module to
draw on a GWindow object.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GLine, GPolygon, GArc
from campy.graphics.gwindow import GWindow


def main():
    window = GWindow(width=800, height=500, title='MyFace')
    face = GOval(200, 250, x=350, y=200)
    face.filled = False
    face.fill_color = 'black'
    face.color = 'red'
    window.add(face)
    l_eye = GOval(50, 50, x=390, y=230)
    l_eye.filled = True
    l_eye.fill_color = 'brown'
    window.add(l_eye)
    r_eye = GOval(50, 50, x=450, y=230)
    r_eye.filled = True
    r_eye.fill_color = 'brown'
    window.add(r_eye)
    mouth = GRect(120, 40, x=390, y=360)
    window.add(mouth)
    label = GLabel('Hi', x=100, y=200)
    label.font = '-40'
    label.color = 'magenta'
    window.add(label)


if __name__ == '__main__':
    main()

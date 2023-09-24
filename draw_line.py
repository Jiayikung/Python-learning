"""
File: draw_line.py
Name: Doris
-------------------------
This program allows users to simulate a game that will create a line between two hollow circles,
with each click indicating the position of a hollow circle.
This program also provides an example of the use of global variables.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the radius of the hollow circle
SIZE = 5

# Global Variable
window = GWindow()
click1 = None  # The odd times of click
click2 = None  # The even times of click
is_the_even_click = False  # Used as a switch in the following codes
circle = GOval(SIZE * 2, SIZE * 2)  # Create a hollow circle


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(event):
    global is_the_even_click
    circle.filled = True
    circle.fill_color = 'white'
    # Only run through the codes below when the odd times of clicks occur
    if not is_the_even_click:
        window.add(circle, x=event.x - SIZE, y=event.y - SIZE)
        is_the_even_click = True  # Turn off the switch
    else:
        # create a line between these two clicks
        line = GLine(circle.x, circle.y, event.x, event.y)
        line.color = 'black'
        window.add(line)
        window.remove(circle)
        is_the_even_click = False  # Turn on the switch to start a new round


if __name__ == "__main__":
    main()

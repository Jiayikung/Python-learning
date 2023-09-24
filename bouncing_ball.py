"""
File: bouncing_ball.py
Name: Doris
-------------------------
This program simulates a ball's bouncing process for limited rounds.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Constant
VX = 3  # x velocity
DELAY = 10  # the pause time of each move (ms)
GRAVITY = 1  # the velocity of gravity
SIZE = 20  # the diameter of the ball
REDUCE = 0.9  # the proportion of vertical speed remaining after each rebound
START_X = 30  # the starting horizontal position of the ball
START_Y = 40  # the starting vertical position of the ball
ROUND = 3  # should be how many rounds in total

# Global Variable
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
touch_wall = False  # Used as a switch in the following codes
count = 0  # count how many round


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global touch_wall, count
    onmouseclicked(bouncing)
    ball.filled = True
    window.add(ball)
    vy = 0  # y velocity
    while True:
        if touch_wall and count < ROUND:
            # enter the new round
            while True:
                if ball.x + ball.width > window.width:
                    break
                ball.move(VX, vy)
                # change ball's moving direction when reaching the bottom and the velocity of y is positive
                if ball.y + ball.height >= window.height and vy > 0:
                    vy = -(vy*REDUCE)
                vy += GRAVITY
                pause(DELAY)
            # exit
            count += 1
            touch_wall = False
            ball.x = START_X
            ball.y = START_Y
            vy = 0
        pause(DELAY)


def bouncing(event):
    global touch_wall
    touch_wall = True  # Turn off the switch to prevent activating another round during the game


if __name__ == "__main__":
    main()

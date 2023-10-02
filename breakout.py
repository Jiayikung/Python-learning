"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.
===========================================
This is the file that uses the BreakoutGraphics class for the breakout game
"""

from campy.graphics.gobjects import GLabel
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second


def main():
    graphics = BreakoutGraphics()


    while True:
        pause(FRAME_RATE)
        # Begin the next round only while the mouse is clicked and there are remaining lives
        while graphics.is_clicked and graphics.lives > 0 and graphics.brick_qty > 0:
            # Each round should update horizontal & vertical speeds for the ball
            dx = graphics.dx()
            dy = graphics.dy()
            pause(FRAME_RATE)
            # Set up the exit condition: exit when the ball falls below the bottom of the window
            if graphics.ball.y >= graphics.window.height-graphics.ball.height:
                graphics.lives -= 1
                graphics.reset_position()  # Reset the ball's position and speeds, and also turn off the switch
                graphics.lives_label.text = 'Lives: ' + str(graphics.lives)  # Update the lives_label
                break

            # Update the movement
            graphics.ball.move(dx, dy)

            # Check for rebound scenarios:
            # Scenario1. If touched the paddle or bricks
            graphics.check_collision()

            # Scenario2. If touched the walls
            if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
                graphics.dx = -dx  # Use setter to update the horizontal speeds for the ball
            if graphics.ball.y <= 0 or graphics.ball.y+graphics.ball.height >= graphics.window.height:
                graphics.dy = -dy



if __name__ == '__main__':
    main()

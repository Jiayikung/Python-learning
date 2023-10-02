"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.
===========================================
This is the file that designs the BreakoutGraphics class for the breakout game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
INITIAL_SCORE = 0      # Initial score of the game
NUM_LIVES = 3			# Number of attempts


class BreakoutGraphics:
    # Constructor
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, score=INITIAL_SCORE,
                 title='Breakout'):
        self.paddle_offset = paddle_offset
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.ball_radius = ball_radius
        self.score = score
        self.brick_qty = brick_cols * brick_rows

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height,
                            x=(window_width-paddle_width)/2,
                            y=window_height-paddle_offset-paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Create the lives label
        self.lives = NUM_LIVES
        self.lives_label = GLabel('Lives:' + str(self.lives))
        self.lives_label.font = 'Courier-25-bold-italic'
        self.lives_label.color = 'turquoise'
        self.window.add(self.lives_label, x=0, y=self.lives_label.height + 5)

        # Create a score label
        self.score_label = GLabel('Scores:' + str(self.score) + '/100')
        self.score_label.font = 'Courier-25-bold-italic'
        self.score_label.color = 'magenta'
        self.window.add(self.score_label, window_width-self.score_label.width, self.score_label.height+5)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2,
                          x=(window_width-ball_radius*2)/2,
                          y=(window_height-ball_radius*2)/2)
        self.ball.filled = True
        self.window.add(self.ball)

        # Draw bricks
        for row in range(brick_rows):
            for col in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if row % 10 <= 1:
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                elif row % 10 <= 3:
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                elif row % 10 <= 5:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                elif row % 10 <= 7:
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                elif row % 10 <= 9:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                self.window.add(self.brick, x=(brick_width+brick_spacing)*col,
                                y=(brick_height+brick_spacing)*row+brick_offset)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.ball_velocity()

        # Initialize our mouse listeners
        self.is_clicked = False  # used as a switch for the 'onmouseclicked' event
        onmousemoved(self.paddle_move)
        onmouseclicked(self.start_new_round)

    # Instance methods
    def ball_velocity(self):
        """
        This method is used to randomly choose horizontal & vertical speed for the ball.
        We also assume if the possibilities are larger than 0.5, the ball will move in the opposite direction.
        :return: A series of codes
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def paddle_move(self, event):
        """
        Whenever the mouse moves, this method will move the paddle horizontally in line with the x-axis of the mouse.
        That is to say, the paddle's middle point will equal to the x-axis of the mouse.
        :param event: The information of onmounsemoved package
        :return: A series of codes
        """
        self.paddle.y = self.window.height-self.paddle_offset
        if self.paddle_width/2 <= event.x <= self.window.width - self.paddle_width/2:
            self.paddle.x = event.x-(self.paddle_width/2)

    def start_new_round(self, event):
        """
        While the mouse clicking, the game will start a new round by turning on the switch.
        :param event: The information of onmounseclicked package
        :return: A series of codes
        """
        self.is_clicked = True  # Turn on the switch

    @property
    def dx(self):  # The getter for the horizontal speed for the ball
        return self.__dx

    @property
    def dy(self):  # The getter for the vertical speed for the ball
        return self.__dy

    @dx.setter
    def dx(self, new_dx):  # The setter for the horizontal speed for the ball
        self.__dx = new_dx

    @dy.setter
    def dy(self, new_dy):  # The setter for the vertical speed for the ball
        self.__dy = new_dy

    def reset_position(self):
        """
        This method is used to: 1. set the ball's position to the middle of the window,
        2. reset both the horizontal and vertical speed of the ball, and
        3. turn off the switch when exiting a round of the game.
        :return:  A series of codes
        """
        x = (self.window.width - (self.ball_radius * 2)) / 2
        y = (self.window.height - (self.ball_radius * 2)) / 2
        self.ball.x = x
        self.ball.y = y
        self.ball_velocity()  # Reset the speeds
        self.is_clicked = False  # Turn off the switch

    def check_collision(self):
        """
        This method is used to check whether there's a collision event.
        And if there is, what's the collided object?
        1) If the collided object is a paddle, then the ball rebounds by changing the vertical speed.
        2) If the collided object is brick, then the ball rebounds and the bricks will be removed.
        :return:
        """
        # Check each 4 corner points of the ball: (x,y), (x, y+2r), (x+2r, y), (x+2r, y+2r)
        for i in [0, 2]:
            for j in [0, 2]:
                obj = self.window.get_object_at(self.ball.x+i*self.ball_radius,
                                                self.ball.y+j*self.ball_radius)
                if obj is not None and obj is not self.score_label and obj is not self.lives_label:  # If there's a collision event
                    if obj is self.paddle:  # And the collided object is a paddle
                        if self.__dy >0:
                            self.__dy = -self.__dy
                        return
                    else:  # And the collided object is brick
                        self.window.remove(obj)
                        self.__dy = -self.__dy
                        self.brick_qty -= 1
                        self.score += 1
                        self.score_label.text = 'Scores:' + str(self.score) + '/100'
                        return

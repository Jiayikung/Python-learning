from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked
import random

# users can change the value -> keyword argument
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
ZONE_WIDTH = 100
ZONE_HEIGHT = 100
BALL_RADIUS = 15
# users cannot change the value
MAX_SPEED = 6
MIN_Y_SPEED = 2


class ZoneGraphics:
    # constructor
    def __init__(self, window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT,
                 zone_width=ZONE_WIDTH, zone_height=ZONE_HEIGHT, ball_radius=BALL_RADIUS):
        # Create window
        self.window = GWindow(width=window_width, height=window_height, title='zone game')
        # Create zone
        self.zone = GRect(width=zone_width, height=zone_height, x=(window_width-zone_width)/2,
                          y=(window_height-zone_height)/2)
        self.zone.color = 'blue'
        self.window.add(self.zone)
        # Create ball and initialize velocity/position
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.reset_ball()
        # Initialize mouse listeners
        onmouseclicked(self.handle_click)
        self.dx = 0
        self.dy = 0

    def handle_click(self, event):
        obj = self.window.get_object_at(event.x, event.y)
        if obj == self.ball:
            self.reset_ball()

    def reset_ball(self):
        """
        Used to reset the ball's position
        ========================================
        Since I need to use 'ball' variable,
        I have to adjust the name as 'self.ball' in the above section
        and then used as 'self.ball' in the following section.
        Also need to adjust the method as 'self.reset_ball' in the above section
        if you want to use self method when create class.
        """
        self.set_ball_position()
        while self.ball_in_zone():
            self.set_ball_position()
        self.set_ball_velocity()
        self.window.add(self.ball)  # adjust as 'self.window' in the above section

    def set_ball_position(self):
        """
        Used to change the position of the ball
        """
        self.ball.x = random.randint(0, self.window.width-self.ball.width)
        self.ball.y = random.randint(0, self.window.height-self.ball.width)

    def ball_in_zone(self):
        """
        result: boolean, whether ball is in zone or not
        """
        zone_left_side = self.zone.x  # adjust as 'self.zone' in the above section
        zone_right_side = self.zone.x + self.zone.width
        is_ball_x_in_zone = zone_left_side <= self.ball.x <= zone_right_side-self.ball.width  # boolean

        zone_top = self.zone.y
        zone_bottom = self.zone.y+self.zone.height
        is_ball_y_in_zone = zone_top <= self.ball.y <= zone_bottom-self.ball.height  # boolean

        return is_ball_x_in_zone and is_ball_y_in_zone

    def set_ball_velocity(self):
        # set as 'self.dx' and 'self.dy' to store this critical variable
        self.dx = random.randint(0, MAX_SPEED)  # use 'MAX_SPEED' because it value is not available to change
        self.dy = random.randint(MIN_Y_SPEED, MAX_SPEED)
        if random.random() > 0.5:  # If possibilities > 0.5, then ball starts to shift left
            self.dx = -self.dx
        if random.random() > 0.5:
            self.dy = -self.dy

    @staticmethod
    def get_vx():
        return random.randint(0, MAX_SPEED)

    @staticmethod
    def get_vy():
        return random.randint(MIN_Y_SPEED, MAX_SPEED)

    # def set_ball_position(self):
    #     random_x = random.randint(0, self.window.width-self.ball.width)
    #     random_y = random.randint(0, self.window.height-self.ball.height)
    #     self.ball.x = random_x
    #     self.ball.y = random_y


from campy.graphics.gobjects import GOval, GRect

print('__name__ :' + str(__name__))


class Robot:
    # Constructor
    def __init__(self, height, weight, color='green'):
        self.h = height
        self.w = weight
        self.c = color

    @staticmethod
    def say_hi():
        print('Hi')
    # def say_hi(self):
    #     print('Hi')
    # @classmethod
    # def say_hi(cls):
    #     print('Hi')

    # Method
    def give_me_a_ball(self, size):
        ball = GOval(size, size)
        ball.filled = True
        ball.fill_color = self.c
        return ball

    def self_intro(self):
        print(f'h={self.h}/w={self.w}')

    def bmi(self):
        h_in_meter = self.h/100
        print('bmi:', self.w/(h_in_meter**2))


class Robot2(Robot):
    def __init__(self, height2, weight2, color2='green', count2=3):
        super().__init__(height2, weight2, color=color2)
        self.count = count2

    def start_count(self):
        for i in range(self.count):
            print(i+1)


class Robot3(Robot2):
    def __init__(self, height3, weight3, rect_color3,
                 color3='green', count3=3):
        super().__init__(height3, weight3, color2=color3,
                         count2=count3)
        self.r_c = rect_color3

    def give_me_a_rect(self,size):
        rect = GRect(size, size)
        rect.filled = True
        rect.fill_color = self.r_c
        return rect

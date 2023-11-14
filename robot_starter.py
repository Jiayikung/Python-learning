from robot import Robot, Robot2, Robot3
from campy.graphics.gwindow import GWindow

print('__name__ :' + str(__name__))
# __name__ :robot
# __name__ :__main__


def main():
    # window = GWindow()
    # r1 = Robot(160, 50)
    # r2 = Robot(183, 65, color='magenta')
    # # instance method
    # ball1 = r1.give_me_a_ball(500)
    # ball2 = r2.give_me_a_ball(350)
    # window.add(ball1)
    # window.add(ball2)
    # r1.self_intro()
    # r2.self_intro()
    # r1.bmi()
    # r2.bmi()
    # # static method
    # Robot.say_hi()
    # r1.say_hi()
    # r2.say_hi()

    # window = GWindow()
    # r2 = Robot2(183, 70, color2='tomato', count2=5)
    # r2.start_count()
    # r2.say_hi()
    # r2.self_intro()
    # ball2 = r2.give_me_a_ball(400)
    # window.add(ball2)

    window = GWindow()
    r3 = Robot3(180, 100, 'blue')
    rect = r3.give_me_a_rect(400)
    ball = r3.give_me_a_ball(250)
    window.add(rect)
    window.add(ball)



if __name__ == '__main__':
    main()
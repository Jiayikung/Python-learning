"""
File: class_reviews.py
Name: Doris
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

# This number controls when to exit the system
EXIT = -1


def main():
    """
    After repeatedly inputting new scores for course SC001 or SC101,
    this program helps find the maximum score, the minimum score, and the average score for both courses.
    Also, the user can stop the game whenever inputting certain number as 'EXIT'
    """
    course = input('Which class? ').upper()
    # If having wrong format, keep asking user to input answers until getting correct one
    while course != 'SC001' and course != 'SC101' and course != str(EXIT):
        print('Wrong format!')
        course = input('Which class? ').upper()
    # Exit the system as long as the inputting answer equals to the value of 'EXIT'
    if course == str(EXIT):
        print('No class scores were entered')
    else:
        count1 = 0
        count2 = 0
        score = int(input('Score: '))
        if course == 'SC001':
            maximum1 = score
            minimum1 = score
            total_sum1 = score
            count1 += 1
        elif course == 'SC101':
            maximum2 = score
            minimum2 = score
            total_sum2 = score
            count2 += 1

        while True:
            course = input('Which class? ').upper()
            while course != 'SC001' and course != 'SC101' and course != str(EXIT):
                print('Wrong format!')
                course = input('Which class? ').upper()
            if course == str(EXIT):
                break
            score = int(input('Score: '))
            if course == 'SC001':
                if count1 == 0:
                    maximum1 = score
                    minimum1 = score
                    total_sum1 = score
                    count1 += 1
                else:
                    if score > maximum1:
                        maximum1 = score
                    elif score < minimum1:
                        minimum1 = score
                    total_sum1 += score
                    count1 += 1
            elif course == 'SC101':
                if count2 == 0:
                    maximum2 = score
                    minimum2 = score
                    total_sum2 = score
                    count2 += 1
                else:
                    if score > maximum2:
                        maximum2 = score
                    elif score < minimum2:
                        minimum2 = score
                    total_sum2 += score
                    count2 += 1

        if count1 != 0:  # average number is undefined if the denominator equals to zero
            average1 = total_sum1 / count1
        if count2 != 0:
            average2 = total_sum2 / count2

        print('=============SC001=============')
        if count1 == 0:
            print('No score for SC001')
        else:
            print('Max(001): ' + str(maximum1))
            print('Min(001): ' + str(minimum1))
            print('Avg(001): ' + str(average1))

        print('=============SC101=============')
        if count2 == 0:
            print('No score for SC101')
        else:
            print('Max(101): ' + str(maximum2))
            print('Min(101): ' + str(minimum2))
            print('Avg(101): ' + str(average2))




# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()

import pypal


def bank():
    jerry_a = pypal.Pypal('YangHung', money=1000, withdraw_limit=700)
    # jerry_a._w_l = 1000
    jerry_a.set_limit(1000)
    jerry_amount = jerry_a.get_remaining()
    print(jerry_amount)
    jerry_a.withdraw(1000)
    jerry_a.withdraw(700)
    jerry_a.withdraw(700)


if __name__ == '__main__':
    bank()
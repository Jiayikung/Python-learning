
WITHDRAW_LIMIT = 1000
MONEY = 0


class Pypal:
    def __init__(self, name, money=MONEY, withdraw_limit=WITHDRAW_LIMIT):
        self._n = name
        self.__m = money
        self._w_l = withdraw_limit


    def set_limit(self, new_limit):
        self._w_l = new_limit

    def get_remaining(self):
        return self.__m

    def withdraw(self, amount):
        if amount > self.__m:
            print('Exceed Limit')
        elif amount > self._w_l:
            print('Error')
        else:
            self.__m -= amount
            print(f"{self._n} remains: {self.__m}")

    def __str__(self):  # ToString Method
        return f'name: {self._n} / money:{self.__m} / limit: {self._w_l}'


def main():
    jerry_a = Pypal('YangHung', 1000, 700)
    print(jerry_a)


if __name__ == '__main__':
    main()


if __name__ == 'pypal':
    print('This Pypal class simulates an online bank account, thanks for using!')
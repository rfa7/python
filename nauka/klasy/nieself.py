class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.x = 100
        self.y = 100

    def zielony(self):
        if self.x == 0:
            print('czerwony')
        elif self.x == 100:
            print('zresetowany')
            return 'zresetowany'
        else:
            print('zielony')

    def __str__(self):
        return "({}, {})".format(self.x, self.y)



class Servo():
    """
        Stub Servo
    """

    def __init__(self, board, index):
        self.board = board
        self.index = index
        self._position = 0

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        assert -1 <= position <= 1
        print("Setting servo {} on {} to {} degrees.".format(self.index, self.board._serial, position))
        self._position = position


class ServoBoard():
    """
        Stub Servo Board
    """

    def __init__(self, serial):
        self._serial = serial
        self.servos = {}
        for i in range(15):
            self.servos[i] = Servo(self, i)

class Motor():
    """
        Stub Motor
    """

    def __init__(self, board, motor_name):
        self.board = board
        self.motor_name = motor_name
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        print("Setting {} on board {} to {}.".format(self.motor_name, self.board._serial, voltage))


class MotorBoard()
    """
        Stub Motor Board
    """

    def __init__(self, serial):
        self._serial = serial
        self.m0 = Motor(self, "m0")
        self.m1 = Motor(self, "m1")

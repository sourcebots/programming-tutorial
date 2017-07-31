from enum import Enum
import random


class PinMode(Enum):
    INPUT = 'hi-z'
    INPUT_PULLUP = 'pullup'
    OUTPUT_HIGH = 'high'
    OUTPUT_LOW = 'low'


class PinValue(Enum):
    HIGH = 'high'
    LOW = 'low'


class Gpio():
    def __init__(self, board, pin):
        self._pin = pin
        self._board = board
        self._mode = PinMode.INPUT

    @property
    def mode(self):
        return self._pin

    @mode.setter
    def mode(self, mode):
        print("Setting GPIO pin {} on board {} to {}.".format(self._pin, self._board, mode))
        self._mode = mode

    def read(self):
        return random.choice([PinValue.HIGH, PinValue.LOW])


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

        self.gpios = {}
        for i in range(2, 13):
            self.gpios[i] = Gpio(self, i)

    def read_ultrasound(self, trigger_pin, echo_pin):
        return random.randint(0, 1000) / 1000

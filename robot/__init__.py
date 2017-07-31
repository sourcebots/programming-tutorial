from robot.game_specific import *
from robot.motor import MotorBoard
from robot.servo import ServoBoard
from robot.power import PowerBoard

BRAKE = 0
COAST = 'coast'

motor0 = MotorBoard('SB123')
motor1 = MotorBoard('SB456')
servo0 = ServoBoard('SBABC')
power = PowerBoard('SBDEF')


class Robot():
    motor_boards = {
        'SB123': motor0,
        'SB456': motor1,
        0: motor0,
        1: motor1
    }

    servo_boards = {
        'SBABC': servo0,
        0: servo0
    }

    power_boards = {
        'SBDEF': power,
        0: power
    }

    def __init__(self):
        self.motor_board = self.motor_boards[0]
        self.servo_board = self.servo_boards[0]
        self.power_board = self.power_boards[0]
        self.zone = 1
        self.mode = GameMode.COMPETITION

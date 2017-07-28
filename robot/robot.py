from robot.motor import MotorBoard
from robot.servo import ServoBoard
from robot.camera import Camera
from robot.power import PowerBoard

motor0 = MotorBoard('SB123')
motor1 = MotorBoard('SB456')
servo0 = ServoBoard('SBABC')
camera = Camera('SB789')
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

    cameras = {
        'SB789': camera,
        0: camera
    }

    power_boards = {
        'SBDEF': power,
        0: power
    }

    def __init__(self):
        self.motor_board = self.motor_boards[0]
        self.servo_board = self.servo_boards[0]
        self.power_board = self.power_boards[0]
        self.camera = self.cameras[0]

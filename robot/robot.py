from robot.motor import MotorBoard
from robo.servo import ServoBoard
from robot.camera import Camera

motor0 = MotorBoard('SB123')
motor1 = MotorBoard('SB456')
servo0 = ServoBoard('SBABC')
camera = Camera('SB789')

def get_first(d):
    return d[list(d.keys())[0]]

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
        'SB789': camera
    }

    def __init__(self):
        self.motor_board = get_first(self.motor_boards)
        self.servo_board = get_first(self.servo_boards)
        self.camera = get_first(self.cameras)

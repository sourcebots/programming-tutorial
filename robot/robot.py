from robot.motor import MotorBoard
from robo.servo import ServoBoard

motor0 = MotorBoard('SB123')
motor1 = MotorBoard('SB456')
servo0 = ServoBoard('SBABC')

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

from robot.motor import MotorBoard

motor0 = MotorBoard('SB123')
motor1 = MotorBoard('SB456')

class Robot():
    motor_boards = {
        'SB123': motor0,
        'SB456': motor1,
        0: motor0,
        1: motor1
    }

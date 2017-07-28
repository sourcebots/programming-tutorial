from robot import Robot

robot = Robot()
board = robot.motor_boards[0]
board.m0.voltage = 50

board.m1.voltage = board.m0.voltage



from robot import Robot

robot = Robot()

board = robot.servo_boards[0]

board.servos[0].position = -0.25

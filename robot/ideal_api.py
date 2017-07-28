"""
    Used to test stub implementation
"""

from robot import Robot, COAST, BRAKE

r = Robot()

left_motor = r.motor_boards['SB123'].m0
r.motor_boards['SB123'].m1.voltage = COAST
r.motor_boards[0].m1.voltage = 1.0
r.motor_boards[0].m1.voltage = 0
r.motor_boards[0].m1.voltage = BRAKE
assert r.motor_boards[0].m1.voltage == BRAKE
r.motor_boards[0].m1.voltage = 1
r.motor_boards[0].m1.voltage = -1

r.servo_boards[0].ports[2].position = -1

# Indexing tokens
tokens = r.cameras[0].see()

from robot import Robot, TOKEN

robot = Robot()

markers = robot.camera.see()

token = None

for marker in markers:
    if marker.id in TOKEN:
        token = marker
        break

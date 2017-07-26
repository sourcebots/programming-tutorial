import math
from robot.game_specific import WALL, TOKEN

class PolarCoord:
    def __init__(self, rot, dist_m):
        self.rot_x_rad = rot[0]
        self.rot_y_rad = rot[1]
        self.rot_z_rad = rot[2]
        self.distance_metres = dist_m

    @property
    def rot_x_deg(self):
        return math.degrees(self.rot_x_rad)

    @property
    def rot_y_deg(self):
        return math.degrees(self.rot_y_rad)

    @property
    def rot_z_deg(self):
        return math.degrees(self.rot_z_rad)


class Marker:
    def __init__(self, id, polar):
        self.id = id
        self.polar = PolarCoord(polar[0], polar[1])

    @property
    def distance_metres(self):
        return self.polar.distance_metres

    def is_wall_marker(self):
        return self.id in WALL

    def is_token_marker(self):
        return self.id in TOKEN

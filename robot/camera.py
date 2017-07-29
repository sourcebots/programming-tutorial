from robot.marker import Marker
from random import randint


def build_fake_marker():
    marker_id = randint(1, 6)
    dist = randint(300, 6000) / 1000
    coords = tuple([randint(-90, 90) for i in range(3)])
    return Marker(marker_id, (coords, dist))


class Camera:
    def __init__(self, serial):
        self.serial = serial

    def see(self):
        print("Looking for markers...")
        markers = [build_fake_marker() for i in range(randint(0, 6))]
        print("Found {} markers".format(len(markers)))
        return markers

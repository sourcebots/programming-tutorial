from robot.marker import Marker

MARKERS = [
    {
        'id': 1,
        'polar': (
            (12, 130, 14),
            4.5
        )
    },
    {
        'id': 2,
        'polar': (
            (12, -40, 14),
            3.2
        )
    },
    {
        'id': 4,
        'polar': (
            (12, -40, 0),
            3.2
        )
    },
    {
        'id': 6,
        'polar': (
            (12, 40, 0),
            3.2
        )
    }
]

class Camera:
    def __init__(self, serial):
        self.serial = serial

    def see(self):
        print("Looking for markers...")
        markers = [Marker(**m) for m in MARKERS]
        print("Found {} markers!".format(len(markers)))
        return markers

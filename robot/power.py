class PowerBoard:
    def __init__(self, serial):
        self.serial = serial

    def power_on(self):
        print("Powering on outputs on board {}.".format(self.serial))

    def power_off(self):
        print("Powering off outputs on board {}.".format(self.serial))

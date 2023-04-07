class Computer:


    def __init__(self, name, chip, monitor, origin):
       self.name = name
       self.chip = chip
       self.monitor = monitor
       self.origin = origin

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_chip(self):
        return self.chip

    def set_chip(self, chip):
        self.chip = chip

    def get_monitor(self):
        return self.monitor

    def set_monitor(self, monitor):
        self.monitor = monitor

    def get_origin(self):
        return self.origin

    def set_origin(self, origin):
        self.origin = origin


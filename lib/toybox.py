class Toybox():
    def __init__(self, name):
        self.name = name
        self.storage = []

    def add_toy(self, toy):
        self.storage.append(toy)

    def see_toybox_contents(self):
        return self.storage
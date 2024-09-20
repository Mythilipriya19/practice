class fruit:
    def __init__(self):
        self.rate=10
    def apple(self):
        self.rate+=20
        print(self.rate)
    def colour(self):

        self.colour-=10
        print(self.colour)
    def drive(self):
      self.apple()

obj=fruit()
obj.drive()
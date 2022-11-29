class Car:

    def __int__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("The car is been drive")

    def stop(self):
        print("Car stopped")
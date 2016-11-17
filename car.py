class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = None
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12
    def display_all(self):
        print 'Price:', self.price
        print 'Speed:', self.speed, 'mph'
        print 'Fuel:', self.fuel
        print 'Mileage:', self.mileage, 'mpg'
        print 'Tax:', self.tax

outback = Car(20000, 60, 'Not Full', 25)

mini_cooper = Car(5000, 40, 'Full', 15)

outback.display_all()

mini_cooper.display_all()

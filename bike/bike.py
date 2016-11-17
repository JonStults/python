class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print self.price, self.max_speed, self.miles
    def ride(self):
        self.miles += 10
        print "Riding", self.miles
        return self
    def reverse(self):
        if self.miles >=10:
            self.miles -= 10
            print "Reversing", self.miles
            return self

instance1 = Bike(200, 22, 'travelled')

instance1.ride().ride().reverse().displayInfo()

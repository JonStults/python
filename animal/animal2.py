from animal import Animal
class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health += 70
    def pet(self):
        self.health += 5
        print self.health
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10
        print self.health
        return self


dog1 = Dog('name')

dog1.walk().walk().walk().run().run().pet().displayHealth()

dragon1 = Dragon('Bart')
dragon1.walk().walk().walk().run().run().fly().fly()
print 'this is a dragon!'
dragon1.displayHealth()

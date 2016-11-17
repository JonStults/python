from animal import Animal
class Dog(Animal):
    self.health = 150
    def pet(self):
        self.health += 5
        print self.health
        return self

dog1 = ('Poo', 'health')

dog1.walk().walk().walk().run().run().pet().displayHealth()

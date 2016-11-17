class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health -= 1
        print self.health
        return self
    def run(self):
        self.health -= 5
        print self.health
        return self
    def displayHealth(self):
        print self.name
        print self.health
        return self

if (__name__=='__main__'):

    animal = Animal('Bear')

    animal.walk().walk().walk().run().run().displayHealth()

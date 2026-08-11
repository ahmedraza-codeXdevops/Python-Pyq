class Grandfather:
    def  grandfather_property(self):
        print("Grandfather has a house")

class Father(Grandfather):
    def father_property(self):
        print("Father has a car")

class Son(Father):
    def son_property(self):
        print("Son has a bike")

s = Son()
s.grandfather_property()
s.father_property()
s.son_property()


#An example of a class that makes bicycles
class Bicycle:
    def __init__(self, size, color, noise):
        self.size = size
        self.color = color
        self.noise = noise
        
    def ring_bell(self):
        return self.noise







if __name__ =='__main__':
    bike_1 = Bicycle(5, "red", "Blah")
    print(bike_1.ring_bell())


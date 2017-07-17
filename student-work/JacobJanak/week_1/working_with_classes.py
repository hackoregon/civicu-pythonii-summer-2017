import random

class Zoo:
    noOfAnimals = 0
    noOfZoos = 0
    
    def __init__(self, animals, ticketPrice):
        Zoo.noOfAnimals += len(animals)
        Zoo.noOfZoos += 1
        self.ticketPrice = ticketPrice
        self.animals = animals

    def __iter__(self):
        for animal in self.animals:
            yield animal

    def __str__(self):
        return " ".join(self.animals)

    def randomMate(self):
        num = random.randrange(0, len(self.animals))
        num2 = random.randrange(0, len(self.animals))
        self.mate(self.animals[num], self.animals[num2])

    def mate(self, male, female):
        newAnimal = male[0:2] + female[2:]
        self.animals.append(newAnimal)
        Zoo.noOfAnimals += 1
        print(newAnimal)

if __name__ == '__main__':
    
    pdxAnimals = ['bat', 'lion', 'goats', 'elephant']
    pdxZoo = Zoo(pdxAnimals, 20)

    vanAnimals = pdxAnimals + ['chimp', 'snake', 'beaver']
    vanZoo = Zoo(vanAnimals, 25)

    vanZoo.randomMate()
    
    print(pdxZoo.noOfAnimals)
    print(Zoo.noOfAnimals)


class Person:
    species = 'homo_sapien'
    energy = 0
    satiety = 0

    def __init__(self, height, age, hair_color, food, hour_slept):
        self.height = height
        self.age = age
        self.hair_color = hair_color
        self.food = food
        self.hour_slept = hour_slept

    def eat(self):
        self.satiety += self.food
        if self.satiety > 0.5:
            return 'full'
        else:
            return 'still hungry'

    def sleep(self):
        self.energy += self.hour_slept
        if self.energy < 8:
            return 'still tired'
        else:
            return 'awake'

    def __str__(self):
        return 'is a person'


class Infant(Person):
    def __init__(self, height, age, hair_color, food, hour_slept):
        super().__init__(height, age, hair_color)



if __name__ == '__main__':
    class_inst = Person(1, 1, 'red', 0.3, 8)
    print(help(class_inst))
    # print(Person.__dict__)
    # print(class_inst.eat())
    # print(class_inst.sleep())
    # print(class_inst.__dict__)
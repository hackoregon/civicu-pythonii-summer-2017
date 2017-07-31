class Car:
    num_of_cars = 5
    def __init__(self, color, make, year, hp):
        self.color = color
        self.make = make
        self.year = year
        self.hp = hp

    def car_color(self):
        return self.color

    def num_cars(self):
        if Car.num_of_cars > 0:
            Car.num_of_cars -= 1
            print('The {}, {}, {}, {} are still here in the back of the house.'.format(self.color, self.make, self.year, self.hp))
        else:
            print('The {}, {}, {}, {} is out of stock'.format(self.color, self.make, self.year, self.hp))


class ElectricCar(Car):
    def __init__(self, color, make, year, hp, charge):
        super().__init__(color, make, year, hp)
        self.charge = charge
        Car.num_of_cars -= 1

    def full_charge(self, charge):
        self.charge = charge
        return charge



car_1 = Car('yellow', 'vw', '3000', '90')
e_car = ElectricCar('green', 'Tesla', '2017', '150', 0)
print(car_1.car_color())
print(e_car.full_charge(100))

cool_car = Car('red', 'mercedes', 2017, 300)
cool_car.num_cars()
cool_car.num_cars()
cool_car.num_cars()
cool_car.num_cars()
cool_car.num_cars()
cool_car.num_cars()

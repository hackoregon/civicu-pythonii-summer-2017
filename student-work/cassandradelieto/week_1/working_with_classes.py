<<<<<<< HEAD
#Make the class have at least three attributes in its __init__ method and at least one method that
#combines two of these attributes in some way.

class MealPreparation:
    people_min = 1

    def __init__(self, people, pans, ingredients):
        self.people = people
        self.pans = pans
        self.ingredients = ingredients

    def contents(self):
       MealPreparation.people_min +=2
       return self.people

    def __str__ (self):
        return "A total of {} people are using {} pans and preparing a meal using the follow ingredient(s) {}.".format(self.people, self.pans, self.ingredients)

#print(MealPreparation.__dict__)

if __name__ == '__main__':
    first_meal = MealPreparation(2,3,"meat")
    print(first_meal)
=======
#Make the class have at least three attributes in its __init__ method and at least one method that
#combines two of these attributes in some way.

class MealPreparation:
    people_min = 1

    def __init__(self, people, pans, ingredients):
        self.people = people
        self.pans = pans
        self.ingredients = ingredients

    def contents(self):
       MealPreparation.people_min +=2
       return self.people

    def __str__ (self):
        return "A total of {} people are using {} pans and preparing a meal using the follow ingredient(s) {}.".format(self.people, self.pans, self.ingredients)

#print(MealPreparation.__dict__)

if __name__ == '__main__':
    first_meal = MealPreparation(2,3,"meat")
    print(first_meal)
>>>>>>> upstream/master

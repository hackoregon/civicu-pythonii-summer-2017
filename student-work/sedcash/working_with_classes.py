class Machine:
    number_of_machines = 0

    def __init__(self, name):
        self.name = name
        Machine.number_of_machines += 1

    def start(self):
        print("Hi, I'm " + self.name + " an I am a machine whose starting")

    def stop(self):
        print("Hi, I'm " + self.name + " an I am a machine whose stopping")

class Camera(Machine):
    number_of_camera = 0

    def __init__(self, name):
        super().__init__(name)
        Camera.number_of_camera += 1

    def start(self):
        print("Hi, I'm " + self.name + " an I am a camera whose starting")
    def stop(self):
        print("Hi, I'm " + self.name + " an I am a camera whose stopping")

bob = Machine("Bob")
sed = Camera("Sed")
# # ashley = Camera("Ashley")
#
#
bob.start()
sed.start()

class Person:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
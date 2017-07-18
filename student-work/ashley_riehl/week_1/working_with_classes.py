# class Bicycle:
#     def __init__(self, size, color, noise):
#         self.size = size
#         self.color = color
#         self.noise = noise
#
#     def ring_bell(self):
#         return self.noise

class Window:
    window_count = 0

    def __init__(self, name, height, width, material, status="closed"):
        self.name = name
        self.height = height
        self.width = width
        self.material = material
        self.status = status
        Window.window_count += 1 #set using class name so instance doesn't have permission to overwrite it

    def open(self):
        self.status = "open"
        print("{} is now open.".format(self.name)) #string interpolation

    def close(self):
        self.status = "closed"
        print(self.name + " is now closed.")

class Car_Window(Window):
    def __init__(self, name, height, width, material, status, automatic):
        super().__init__(name, height, width, material, status) #super needed to override a parent class' method
        self.automatic = automatic

    def child_lock(self):
        self.locked = "True"


if __name__ =='__main__':

    # bike_1 = Bicycle(5, "red", "laaa")
    # print(bike_1.ring_bell())

    kitch_window = Window("kitch_window", 5, 10, "glass") #Make an instance of a class
    kitch_window.open()
    # print(kitch_window.status)

    kitch_window.stained = True #add an attribute

    bath_window = Window("bath_window", 10, 15, "plastic")
    bed_window1 = Window("bed_window1", 12, 42, "glass")
    print(kitch_window.window_count)

    malibu_window = Car_Window("malibu", 2, 2, "glass", "closed", True)
    print(malibu_window.name)

import random
def names_func(a_list, size):
    listoflists = []
    for i in range(0,len(a_list)):
        dim = int(i / size)
        if len(a_list)-1 == i:
            if len(a_list)%size==1:
                 dim = int(i / size) - 1
        elif i%size==0:
            listoflists.append([])
        listoflists[dim].append(a_list[i])
    return listoflists
my_list = [1,2,3,4,5,6,7,8,9]
print(names_func(my_list,2))
print(my_list)
random.shuffle(my_list)
print(my_list)
doubles = []

for x in range(1, 13):
    doubles.append('doubles_'+str(x))
print(doubles)

d={}
for x in range(1,10):
        d["string{0}".format(x)]="Hello"
print(d)
print(my_list)
my_list.remove(3)
print(my_list)
my_dict = {}
my_dict['fred'] = 7
print(my_dict)
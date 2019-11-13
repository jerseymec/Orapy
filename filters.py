import random
Num_list = []
for i in range(101):
  Num_list += [random.randint(1,1000)]

print ( list(filter(lambda x: x%3 == 0, Num_list)))
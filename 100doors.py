

import math

num_of_doors = input("How many doors do you want to play with? ")
num_of_doors1 = int(num_of_doors)
f = int(math.sqrt(num_of_doors1))


print ("The following doors are open: ", end= "")
for i in range(1, f + 1):
    if i == f:
        print(str(i*i))
    else:
        print ((i*i) , end= ',' )



import math


num_of_doors1 = 100
f = int(math.sqrt(num_of_doors1))


print ("The following doors are open: ", end= "")
for i in range(1, f + 1):
    if i*i == 100:
        print(str(i*i))
    else:
        print ((i*i) , end= ',' )

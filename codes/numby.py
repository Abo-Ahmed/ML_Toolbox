

# tensor is a multidimenstional arry designed for keras for better performance
# scalar tensor contains only one number

import numpy as np

def show(item):
    # variable name
    print("\n".join(["#" * 15 + "\nITEM: " + name for name, value in globals().items() if value is item]))

    print("type: " + str(item.dtype))
    print("dimentions: " + str(item.ndim))
    print("shape: " + str(item.shape))

x = np.array(12)
y = np.array([[12 , 3 , 6 , 14] , [2 , 4 , 3 , 5] ] )
show(x)
show(y)

# code to convert np array to anther type
x = x.astype(float)





# temp codes 
# for name, value in globals().items():
#     if value is item:
#         print("#" * 15 + "\nITEM: " + name)
#         break

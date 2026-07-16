# Dyanamic array

import ctypes

class my_list:
    def __init__(self):
        self.size = 1
        self.n = 0
    # creat a c type array with = self.size
        self.A = self.__make_array_(self.size)
    #Add len function
    def __len__(self):
        return self.n
        
    def __make_array_(self, capacity):
        return(capacity*ctypes.py_object)
    
new = my_list()
print(new)
print(len(new))
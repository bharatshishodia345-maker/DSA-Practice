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
    
    #print Array
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result+str(self.A[i]) + ','
        if self.n == 0:
            print("Data is clear")
        
        return '['+ result[:-1] + ']'
     
    #Indexing 
    def __getitem__(self,index):
         if 0<=index < self.n:
             return self.A[index]
         else:
             return 'Index error -> Index out of range ' 
            
    #Apend number
    def append(self, item):
        if self.n == self.size:
            #resize
            self.__resize(self.size*2)
        #append
        self.A[self.n] = item
        self.n = self.n + 1
    
    #pop Item
    def pop(self):
        if self.n == 0:
            print("List Is Empty")
            
        print(self.A[self.n - 1])
        self.n = self.n-1
    
    #Clear all Item
    def clear(self):
        self.size = 1
        self.n = 0
        
    
    def __resize(self, new_capacity):
        # create a new arr with new_capacity
        B = self.__make_array_(new_capacity)
        self.size =new_capacity
        # copy the content of A into B
        for i in range(self.n):
            B[i] = self.A[i]

        self.A = B
        
    def __make_array_(self, capacity):
        return(capacity*ctypes.py_object)()
    
new = my_list()


new.append(88)
new.append('hellow')
new.append(5)
new.append(6)
print(len(new))
new.clear()
print(new)

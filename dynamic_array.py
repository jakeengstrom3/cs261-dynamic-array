# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# YOUR NAME
import numpy as np
class DynamicArray:
    
    def __init__(self):
        self.capacity = 10
        self.data = np.empty(10, dtype=object)
    
    def __getitem__(self, index):
        return self.data[index]

    def is_empty(self):
        
        for x in self.data:
            if x is not None:
                return False

        return True
        
        
    def __len__(self):
        i = 0
        while i < self.data.size:
            if self.data[i] is None: #Finds the first instance of None, prints the index bc that will be the length
                return i

    def append(self, n):
        i = 0
        while i < self.data.size:
            if self.data[i] is None: #Puts the data in the first instance of None
                self.data[i] = n
                return
            i += 1
        print("DynamicArray Full.  Cannot append")

        

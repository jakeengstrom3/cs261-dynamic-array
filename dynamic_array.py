# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# YOUR NAME
import numpy as np
class DynamicArray:
    
    def __init__(self):
        self.capacity = 10
        self.length = 0
        self.array = np.array([])
    
    def __getitem__(self, index):
        return self.array[index]

    def is_empty(self):
        if self.length == 0:
            return True
        return False
        
    def __len__(self):
        return self.length

    def append(self, n):
        if self.length < self.capacity:
            self.length += 1
            self.array = np.concatenate((self.array, [n]))
            return      
        raise Exception("Array at capacity, cannot append")
        

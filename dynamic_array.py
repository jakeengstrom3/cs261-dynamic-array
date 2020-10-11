# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# YOUR NAME
import numpy as np
class DynamicArray:
    
    def __init__(self):
        self.capacity = 10
        self.data = np.empty(self.capacity, dtype=object)
        self.next_index = 0
    
    def __getitem__(self, index):
        if index >= len(self) or index < 0:
            raise IndexError("Index Out of Bounds")
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
            i += 1

    def append(self, n):
        if self.next_index >= self.capacity:
            raise IndexError("DynamicArray Full.  Cannot append")
        self.data[self.next_index] = n
        self.next_index += 1

    def clear(self):
        self.data = np.empty(self.capacity, dtype=object)
        self.next_index = 0

    def pop(self):
        if self.is_empty():
            raise IndexError("Array Empty. Cannot Pop")

        index = self.next_index - 1 #Gets the appropriate index
        target = self.data[index] #Stores the data to be returned
        self.data[index] = None #Removes the element from the array
        self.next_index -= 1 #Moves the next index back
        return target #Returns the element
            
    def delete(self, i):
        if self.is_empty():
            raise IndexError("Array Empty.  Cannot Delete")
        if i >= len(self):
            raise IndexError("Index out of Bounds")
        
        while i < len(self) - 1:
            self.data[i] = self.data[i+1]
            i += 1
        
        self.data[i] = None

        self.next_index -= 1


    

        

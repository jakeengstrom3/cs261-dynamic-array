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
        return self.next_index

    def increaseCapacity(self):

        self.data = np.concatenate((self.data, np.empty(self.capacity, dtype=object)))
        self.capacity *= 2

    def append(self, n):
        
        if self.is_full():
            
            self.increaseCapacity()

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
        if i >= len(self) or i < 0:
            raise IndexError("Index out of Bounds")
        
        while i < len(self) - 1:
            self.data[i] = self.data[i+1]
            i += 1
        
        self.data[i] = None
        self.next_index -= 1
        return self.data[i]

    def insert(self, index, x):
        #Loop from end.  last is last -1, and so on until at i.  i+1 = i, then i = n
        if self.is_full():
            self.increaseCapacity()
        if index < 0 or index > self.capacity:
            raise IndexError("Index out of Bounds")

        i = len(self)
        while i > index:
            self.data[i] = self.data[i - 1]
            i -= 1
        
        self.data[i] = x
        self.next_index += 1
        return x

    def is_full(self):
        return self.next_index >= self.capacity 

    def max(self):
        if self.is_empty():
            return None
        i = 1
        max = self.data[0]
        while i < len(self):
            if(max < self.data[i]):
                max = self.data[i]
            i += 1
        return max

    def min(self):
        if self.is_empty():
            return None
        i = 1
        min = self.data[0]
        while i < len(self):
            if(min > self.data[i]):
                min = self.data[i]
            i += 1
        return min

    def sum(self):
        if self.is_empty():
            return None
        i = 0
        sum = 0
        while i < len(self):
            sum += self.data[i]
            i += 1
        return sum

    def linear_search(self, target):
        
        i = 0
        
        while i < len(self):
            if self.data[i] == target:
                return i
            i += 1
        return None

    def binary_search(self, target):
        min = 0
        max = len(self)
        while min <= max:
            middleIndex = int((min + max) / 2)
            middleValue = self.data[middleIndex]
            if target == middleValue:
                return middleIndex
            elif target > middleValue:
                min = middleIndex + 1
            else:
                max = middleIndex -1
        
        return None


        






    

        

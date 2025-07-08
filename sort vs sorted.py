# Using sort() - modifies the original list
fruits = ["banana", "apple", "cherry"]
print("Original list:", fruits)     # Output: ['banana', 'apple', 'cherry']
fruits.sort()  # In-place sorting
print("After sort():", fruits)      # Output: ['apple', 'banana', 'cherry']
//sort is for list only

# Using sorted() - returns a new sorted list
vegetables = ["carrot", "beetroot", "asparagus"]
new_list = sorted(vegetables)  # Creates a new sorted list
print("After sorted():", new_list)          # Output: ['asparagus', 'beetroot', 'carrot']
print("Original list still:", vegetables)   # Output: ['carrot', 'beetroot', 'asparagus']
//sorted is for all data types

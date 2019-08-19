"""
Other than some generic containers like list, Python can also handle containers with specific data types.
Array can be handled in python by module named “array“.
They can be useful when we have to manipulate only a specific data type values.
"""

import array

# initialize
one_array = array.array('i', [1, 2, 3, 4, 5, 55, 33, 9, 3, 3, 55, 81])  # Order Maintained/Duplicates Allowed
print("Printing Array:", one_array)
print("Array Size:", one_array.__sizeof__())
print("Length:", one_array.__len__())
one_array.append(100)  # Appending an Array in Python
print("Printing Appended Array:", one_array)
print()

one_array.pop()  # Removing last element from an Array
print("Printing Array [After Pop()]:", one_array)

# Binary Search
# Moo Joon Park
# CSCI 77800 Fall 2022
# collaborators: None
# consult: GeeksforGeeks

# Recursive binary search method for value x
def bin_search(array, min, max, x):

#check the base case
  if (max >= min):
  
    mid = (min + max) // 2
  
    # check if the middle array value is x
    if array[mid] == x:
      return mid
  
    # check if the middle array value is greater than x
    elif array[mid] > x:
      return bin_search(array, min, mid-1, x)
  
    # check if the middle array value is less than x
    else:
      return bin_search(array, mid + 1, max, x)
      
  else:
    return -1  # the value is not in the array

# sample array and x value
array = [-2, 0, 13, 45, 89, 122, 358, 3429]
x = 0

# calls the method to search the array for the x value
index = bin_search(array, 0, len(array)-1, x)

# returns the index value in the array or states it doesn't exist in the array
if index != -1:
  print("The value of x is at the index value of " + str(index) + ".")
else:
  print("The value of x is not in the array.")

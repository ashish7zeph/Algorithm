# JUGGLING ALGORITHM for Array Rotation

'''
Instead of moving one by one, divide the array in different sets
where number of sets is equal to GCD of n and d and move the elements within sets.
If GCD is 1 as is for the above example array (n = 7 and d =2), then elements
will be moved within one set only, we just start with temp = arr[0] and keep
moving arr[I+d] to arr[I] and finally store temp at the right place.
'''

# Function to left rotate arr[] of size n by d
def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)


# Function to left Rotate arr[] of size n by 1
def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp
         
 
# Utility function to print an array
def printArray(arr,size):
    for i in range(size):
        print ("%d"% arr[i],end=" ")
 
  
# Driver program to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
print('Original Array:')
printArray(arr, 7)
leftRotate(arr, 2, 7)
print('\n\nArray Rotated by 2 blocks:')
printArray(arr, 7)



'''
Time complexity : O(n)
Auxiliary Space : O(1)
'''

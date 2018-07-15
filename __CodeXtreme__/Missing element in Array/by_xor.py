# simpler and efficient logic using Arithmetic XOR

'''
Problem Statement: You are given a list of n integers and these integers are in
                range of 1 to n. There arev no duplicates in list. One of the
                integers is missing in the list.

                < Find the Missing Integer >
'''

'''
Logic:

    1. XOR all the array elements given and let result be X1
    2. XOR all numbers from 1 to n and let result be X2
    3. Now XOR X1 and X2, you get the missing number
    Because when you XOR a no. with itself, it always return 0
    So allast, the number that wouldn't be XOR'd will be missing number.

    Time Complexity = O(n)
'''
# logic for calculating XOR uptill n
def xor1(n):
    temp = 1
    for i in range(2, n+1):
        temp = temp ^ i
    return temp

# logic for calculating XOR of the array
def xor2(arr, size):
    temp = arr[0]
    for i in range(1, size):
        temp = temp ^ arr[i]
    return temp

arr = [5, 2, 4, 1, 6]
size = 5    # means n-1 = 5, that is n will be 6
print('The array is:')
print(arr)

n = size + 1
ans = xor1(n) - xor2(arr, size)
print('\nThe Missing Element in the Array is:', end = ' ')
print(ans)

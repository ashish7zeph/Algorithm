'''
Problem Statement: You are given a list of n integers and these integers are in
                range of 1 to n. There arev no duplicates in list. One of the
                integers is missing in the list.

                < Find the Missing Integer >
'''

'''
Logic:

    sum of list n-1 is calculated and subtracted from sum upto n
    ans = n(n+1)/2 - sum(array)

    Time Complexity = O(n)
'''

# logic for sum of array
def sum_(arr):
    temp = 0
    for i in arr:
        temp += i
    return temp

arr = [5, 2, 4, 1, 6]
size = 5    # means n-1 = 5, that is n will be 6
print('The array is:')
print(arr)

n = size + 1
ans = (n*(n+1))//2 - sum_(arr)
print('\nThe Missing Element in the Array is:', end = ' ')
print(ans)

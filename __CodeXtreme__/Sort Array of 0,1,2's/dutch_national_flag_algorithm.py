# Python program to sort an array with 0,1 and 2 in a siingle pass
'''
Logic:

    1. Lo := 1; Mid := 1; Hi := N;
    2. while Mid <= Hi do
        1. Invariant: a[1..Lo-1]=0 and a[Lo..Mid-1]=1 and a[Hi+1..N]=2; a[Mid..Hi] are unknown.
        2. case a[Mid] in
             0: swap a[Lo] and a[Mid]; Lo++; Mid++
             1: Mid++
             2: swap a[Mid] and a[Hi]; Hi–-
             
    Time Complexity : O(n)
'''

# Function to sort array
def sort012( a, arr_size):
    lo = 0
    hi = arr_size - 1
    mid = 0
    while mid <= hi:
        if a[mid] == 0:
            a[lo],a[mid] = a[mid],a[lo]
            lo = lo + 1
            mid = mid + 1
        elif a[mid] == 1:
            mid = mid + 1
        else:
            a[mid],a[hi] = a[hi],a[mid] 
            hi = hi - 1
    return a
     
# Function to print array
def printArray( a):
    for k in a:
        print(k, end = ' ')
    print()
     
 
# Driver Program
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
arr_size = len(arr)
print('Array before segregation:')
printArray(arr)
arr = sort012( arr, arr_size)
print('\nArray after segregation:')
printArray(arr)

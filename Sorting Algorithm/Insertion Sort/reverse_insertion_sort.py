print('Enter space seperated list elements to be reverse sorted')
A = [int(x) for x in input().split()]

#insertion sort algo
for j in range(1, len(A)):
    key = A[j]
    i = j-1
    while(i > -1 and A[i] < key):  #just a small change here
        A[i+1] = A[i]
        i -= 1
    A[i+1] = key

print(A)

#(A[i] < key) is to find the right place of key
#so that left of key has greater values than itself

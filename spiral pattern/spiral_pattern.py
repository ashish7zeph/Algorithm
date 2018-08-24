# source code

import time, os


# main code
def main():

    os.system('color 1f')
    n = int(input('\n  Input size of grid: '))
    a = {}  # dict to store key (a number on the matrix) and value (as its coordinate)
    x = y = 0
    z = n-1
    k = z
    l = 1
    status = 'r'

    for i in range(1, n*n+1):
        a[i] = [x, y]

        if status == 'r': y += 1    # status right
        elif status == 'l': y -= 1  # status left
        elif status == 'u': x -= 1  # status up
        elif status == 'd': x += 1  # status down

        if i == z:
            z = z+k

            if l != 2: l += 1
            elif l == 2:
                l = 1
                k = k-1

            if status == 'r': status = 'd'
            elif status == 'd': status = 'l'
            elif status == 'l': status = 'u'
            elif status == 'u': status = 'r'


    b = []
    c = [' ' for  x in range(n*n)]

    for i in a.items():
        c[n*i[1][0] + i[1][1]] = i[0]

    for i in range(n*n):
        b.append(' '*digits(c[i]))
        
    for i in a.items():
        os.system('cls')
        b[n*i[1][0] + i[1][1]] = i[0]
        print_(b, c, n)
        time.sleep(0.1)
    
    input()
    os.system('cls')
    main()

# function to count digits in a number
def digits(num):
    count = 0
    while num:
        count += 1
        num //= 10
    return count

# function for printing matrix on screen
def print_(_list_, _list2_, n):
    print('\n'*5)
    d = digits(n*n)
    d2 = 0
    
    for i in range(n*n):
        d2 = digits(_list2_[i])
        if (i+1)%n != 0: print(' '*(5+(d-d2))+str(_list_[i]), end = '')
        else: print(' '*(5+(d-d2))+str(_list_[i]), end = '\n'*3)



if __name__ == '__main__':
    main()
    

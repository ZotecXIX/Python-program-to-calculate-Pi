from decimal import *

import time




def process():

    f = open('file.txt','a')

    number = -1
    start = input('Press Enter')

    user_number = input('To how many decimal places do you want it to have?')

    user_number = int(user_number)
    

    while start == '':
        

        opp = 1/number
        opp = str(opp)

        

        getcontext().prec = user_number
        
        

        
        number = number + 2
        pi = (Decimal(4) / Decimal(number))
        number = number + 2
        pi2 = (Decimal(4) / Decimal(number))
        number = number + 2
        pi3 = (Decimal(4) / Decimal(number))
        number = number + 2
        pi4 = (Decimal(4) / Decimal(number))

        print(pi)
        print(pi2)
        print(pi3)
        print(pi4)


        pi = str(pi)
        pi2 = str(pi2)
        pi3 = str(pi3)
        pi4 = str(pi4)
        

        

        f.write(str(pi + '\n'))
        f.write(str(pi2 + '\n'))
        f.write(str(pi3 + '\n'))
        f.write(str(pi4 + '\n'))





def process1():

    f = open('file.txt', 'r+')
    file = f.readlines()
    file = [x.strip() for x in file]

    number = 0
    totalx = 0
    

    start = input('Press Enter')
    user_number = input('To what decimal place do you want to calculate pi to ? (Best to be the same as the one before)')
    user_number = int(user_number)
    

    while start == '':

        getcontext().prec = user_number
        
        a1 = file[number]
        number = number + 1
        a2 = file[number]
        number = number + 1
        a3 = file[number]
        number = number + 1
        a4 = file[number]
        number = number + 1

        a1 = float(a1)
        a2 = float(a2)
        a3 = float(a3)
        a4 = float(a4)

        
        total = (Decimal(a1) - Decimal(a2) + Decimal(a3) - Decimal(a4))

        a1 = file[number]
        number = number + 1
        a2 = file[number]
        number = number + 1
        a3 = file[number]
        number = number + 1
        a4 = file[number]
        number = number + 1

        a1 = float(a1)
        a2 = float(a2)
        a3 = float(a3)
        a4 = float(a4)

        
        total2 = (Decimal(a1) - Decimal(a2) + Decimal(a3) - Decimal(a4))

        totalx = totalx + total + total2

        print(totalx)








user_in = input('do you want to write the components to work out pi or calculate pi? (cal or write)')

if user_in == 'cal':
    
    process1()

elif user_in == 'write':
    process()



#!/usr/bin/env python 3
# -*- encoding:utf-8 -*-
if __name__== "__main__":

a, b, c = int(input()), int(input()), int(input())

sum_1 = a + b
sum_2 = b + c
sum_3 = a + c

ex_check = 0

if sum_1 > c:
    ex_check += 1

if sum_2 > a:
    ex_check += 1
    
if sum_3 > b:
    ex_check += 1


if ex_check == 3:

    if a ** 2 == b ** 2 + c ** 2:
        print("It's right triangle")
    elif b ** 2 == c ** 2 + a ** 2:
        print("It's right triangle")
    elif c ** 2 == a ** 2 + b ** 2:
        print("It's right triangle")
    else:
        pass

    if a == b:
        print('It is isosceles triangle')
    elif a == c:
        print('It is isosceles triangle') 
    elif b == c:
        print('It is isosceles triangle')
    else:
        pass

    if a == b == c:
        print("It's equilateral triangle")
    else:
        pass

else:
    print("The triangle can't exist")
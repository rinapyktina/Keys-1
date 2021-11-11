#!/usr/bin/env python 3
# -*- encoding:utf-8 -*-
if __name__== "__main__":

dot_a_1, dot_b_1, dot_c_1 = float(input()), float(input()), float(input())
dot_a_2, dot_b_2, dot_c_2 = float(input()), float(input()), float(input())

if ((dot_a_1 == 0) and (dot_b_1 == 0)) or ((dot_a_2 == 0) and (dot_b_2 == 0)):
    print('Это не прямые!')
else:
    if (dot_a_1 * dot_b_2 == dot_a_2 * dot_b_1) and (dot_a_1 * dot_c_2 == dot_a_2 * dot_c_1):
        print('Прямые совпадают')
    else:
        if dot_a_1 * dot_b_2 == dot_a_2 * dot_b_1:
            print('Прямые параллельны')
        else:
            X = (dot_c_1 * dot_b_2 - dot_c_2 * dot_b_1) / (dot_b_1 * dot_a_2 - dot_b_2 * dot_a_1)
            Y = (dot_c_2 * dot_a_1 - dot_c_1 * dot_a_2) / (dot_b_1 * dot_a_2 - dot_b_2 * dot_a_1)
            print(x, y)

            


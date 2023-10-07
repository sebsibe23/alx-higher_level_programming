#!/usr/bin/python3
# 10-divisible_by_2.py


def divisible_by_2(strmy_list=[]):
    """show all multiples of 2 in the list"""
    multtwo = []
    for i in range(len(strmy_list)):
        if strmy_list[i] % 2 == 0:
            multtwo.append(True)
        else:
            multtwo.append(False)

    return (multtwo)

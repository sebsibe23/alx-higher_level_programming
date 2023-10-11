#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    vartot_weight = sum([x[1] for x in my_list])
    varweighted_ = sum([x[0]*x[1] for x in my_list])
    return varweighted_ / vartot_weight

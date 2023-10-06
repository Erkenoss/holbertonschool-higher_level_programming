#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) < 1:
        return 0

    sum_weight = 0
    total_weight = 0

    for tup in my_list:
        value = tup[0]
        weight = tup[1]

        sum_weight += value * weight
        total_weight += weight

    if weight != 0:
        average = sum_weight / total_weight
        return average
    else:
        return 0

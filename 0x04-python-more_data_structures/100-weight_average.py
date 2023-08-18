#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_product = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)
    weighted_average = sum_product / total_weight
    return weighted_average

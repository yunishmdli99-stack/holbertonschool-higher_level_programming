#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    c_set = set()
    for i in set_1:
        for j in set_2:
            if i == j:
                c_set.add(i)
    d_set = set()
    for i in set_1:
        if i not in c_set:
            d_set.add(i)
    for j in set_2:
        if j not in c_set:
            d_set.add(j)
    return d_set

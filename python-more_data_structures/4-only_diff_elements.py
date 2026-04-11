#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    c_set = set()
    for i in set_1:
        for j in set_2:
            if i != j:
                c_set.add(i)
    return c_set

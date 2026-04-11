#!/usr/bin/python3
def best_score(a_dictionary):
    m = None
    best = None
    for i in a_dictionary:
        if m < a_dictionary[i]:
        m = a_dictionary[i]
        best = i
    return best

#!/usr/bin/python3
def best_score(a_dictionary):
    m = a_dictionary[0]
    for i in a_dictionary:
        if m < a_dictionary[i]:
        m = a_dictionary[i]
    for i in a_dictionary:
        if m == a_dictionary[i]:
            return i

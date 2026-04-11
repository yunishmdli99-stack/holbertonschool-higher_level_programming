#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    m = None
    best_key = None
    for i in a_dictionary:
        if m is None or a_dictionary[i] > m:
            m = a_dictionary[i]
            best_key = i
    return best_key

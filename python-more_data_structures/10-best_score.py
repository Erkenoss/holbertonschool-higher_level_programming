#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    key_a = None
    value_a = 0
    for key, value in a_dictionary.items():
        if value > value_a:
            key_a = key
            value_a = value
    return key_a

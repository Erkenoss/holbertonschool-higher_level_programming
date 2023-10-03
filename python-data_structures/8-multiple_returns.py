#!/usr/bin/python3
def multiple_returns(sentence):

    if sentence is not None:
        temp_t = (len(sentence), sentence[0])
    else:
        temp_t = (0, None)

    return temp_t

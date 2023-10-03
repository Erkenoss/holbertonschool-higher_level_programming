#!/usr/bin/python3
def multiple_returns(sentence):

    if len(sentence) == 0:
        temp_t = (0, None)
    else:
        temp_t = (len(sentence), sentence[0])

    return temp_t

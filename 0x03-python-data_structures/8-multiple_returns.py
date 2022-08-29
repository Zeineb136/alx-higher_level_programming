#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) < 1:
        length = 0
        first = None
    else:
        length = len(sentence)
        first = sentence[0]
    tuple_s = (length, first)
    return(tuple_s)

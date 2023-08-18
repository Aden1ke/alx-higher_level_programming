#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        new_tu = (0, "None")
    else:
        new_tu = (len(sentence), sentence[0])
    return (new_tu)

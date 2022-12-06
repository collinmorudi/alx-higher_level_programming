#!/usr/bin/python3
def multiple_returns(sentence):

    size = len(sentence)
    ch = sentence[0] if size > 0 else None

    return (size, ch)

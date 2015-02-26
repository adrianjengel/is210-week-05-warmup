#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean."""


def know_what_i_mean(wink, numwink=2):
    """Multiplies certain variables within a sentence.

    Two variables are being created, wink and nudges, which are then
    multiplied by the factor defined in numwink. A string is returned at the
    end.

    Args:
        wink (str): A string variable combined with the strip() function.
        numwink (int): The number of times the variables will be multiplied by.
        nudges (str): The string 'nudge ' is being multiplied by numwink in
        combination with the strip() function.
    Returns:
        retstr (str) which is the string consisting of 'Know what I mean?'
        and 'winks' and 'nudges' inserted via the .format function.
    Example:

        >>> know_what_i_mean('wink ', numwink=2)
        'Know what I mean? wink wink, nudge nudge'

        >>> know_what_i_mean('hint ', numwink=2)
        'Know what I mean? hint hint, nudge nudge'
    """

    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr

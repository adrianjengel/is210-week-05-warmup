#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 04 WK5 warmup - creating functions."""


def too_many_kittens(kittens, litterboxes, catfood):
    """Calculating if we have enough litterboxes and food for all the kittens.

    Args:
        kittens (int): The number of kittens.
        litterboxes (int): The number of available litterboxes.
        catfood (bool): A boolean representing if we have catfood.
    Returns:
        A boolean value that will tell us whether we have too many kittens
        or not enough food.
    Example:

    >>> too_many_kittens(12, 12, False)
    True

    >>> too_many_kittens(13, 12, True)
    True

    >>> too_many_kittens(12, 13, True)
    False

    """
    return not (litterboxes >= kittens and catfood)

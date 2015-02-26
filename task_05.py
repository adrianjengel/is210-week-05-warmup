#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 05 WK5 warmup - creating functions."""


def defaults(my_optional=True, my_required=None):
    """Set a default value in a function definition.

    Args:
        my_optional (bool): By default True.
        my_required (bool): By default no value.
    Returns:
        A boolean value that will return a logical comparison.
    Example:

    >>> defaults(True)
    True

    >>> defaults(True, False)
    False

    >>> defaults(False, False)
    True

    """
    return my_optional is my_required

"""
test_lazySortedList.py
"""

import pytest
from lazySortedList import LazySortedList

def test_init_empty():
    lsl = LazySortedList()
    assert lsl._list == []
    assert lsl._is_sorted

def test_init_not_empty():
    elements = [5, 7, 9]
    lsl = LazySortedList(elements)
    assert lsl._list == elements
    assert not lsl._is_sorted

def test_append_to_empty():
    lsl = LazySortedList()
    lsl.append(-44)
    assert lsl._list == [-44]
    assert not lsl._is_sorted


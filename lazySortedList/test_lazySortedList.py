"""
test_lazySortedList.py
"""

import pytest
from lazySortedList import LazySortedList, UnsortedError

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


def test_binary_search_exception():
    """Note: We sometimes want to test things besides something being true.
    Here, we test that an exception is thrown if trying to binary search
    using an unsorted list."""
    lsl = LazySortedList([8, 2, 5, 7])

    ## Add this afterward, and see that test fails if list is sorted
    # lsl.sort()

    ## Says: code within this block should raise UnsortedError; if not, test fails
    with pytest.raises(UnsortedError):
        lsl.binary_search(5)

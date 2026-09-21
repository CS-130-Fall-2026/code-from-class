"""
test_sorting.py
Contaions tests for sorting.py
pytest:
- only files starting or beginning with "test" are tested
- You can run all test files like this: pytest
- You can run just a single test file: pytest test_sorting.py
"""

import pytest, sorting

## every test is a function starting with "test"
def test_merge_two_full_lists():
    left = [5, 7, 9, 15]
    right = [-4, 6, 8, 12]
    result = sorting.merge(left, right)
    assert result == [-4, 5, 6, 7, 8, 9, 12, 15]


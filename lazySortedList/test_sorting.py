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

######## What are good tests?
## Some tests should test common use cases - works with expected uses
## Some tests should test edge cases
##   - inputs at the boundaries of expected inputs
##   - common examples:
##     - Integer inputs: 0, very large integers, negative integers
##     - Strings: empty string, single characters, digits/special characters, very long strings
##     - Lists: empty list, check whether or not original list is changed, lists with 1 element
##              lists with different types

def test_merge_diff_sizes():
    left = [5, 7, 9, 15]
    right = [8]
    result = sorting.merge(left, right)
    assert result == [5, 7, 8, 9, 15]

def test_merge_one_element_each():
    left = [9]
    right = [8]
    result = sorting.merge(left, right)
    assert result == [8, 9]

def test_merge_one_empty():
    left = [9, 88, 10202]
    right = []
    result = sorting.merge(left, right)
    assert result == [9, 88, 10202]

def test_merge_both_empty():
    left = []
    right = []
    result = sorting.merge(left, right)
    assert result == []

## Lots of duplicated code. Bad
## We can combine tests using @pytest.mark.parametrize
## Note: Things starting with @ in Python are *decorators*
##       Decorator -- changes the function that follows it.
## @pytest.mark.parametrize requires 2 arguments:
##  1. String of the names of the parameters to the test function
##  2. List of tuples to pass as inputs to the test function
@pytest.mark.parametrize("left, right, expected", [
    ([1, 5, 6, 8], [2, 7, 12, 15], [1, 2, 5, 6, 7, 8, 12, 15]),
    ([1, 2], [6], [1, 2, 6]),
    ([], [], []),
    # ([5, 6], [1, 2], [5, 6, 1, 2]),
    # ([1], [1], [2])
])
def test_merge(left, right, expected):
    result = sorting.merge(left, right)
    assert result == expected


## parametrize has optional 3rd argument: a list of IDs for the tests
@pytest.mark.parametrize("lst, width, expected", [
    ([5, 6, 1, -1, 77, 12, 13, 14], 1, [5, 6, -1, 1, 12, 77, 13, 14]),
    ([2,5,1,7,4,8,3,6], 2, [1, 2, 5, 7, 3, 4, 6, 8]),
    # ([2,5,1,7,4,8,3,6], 2, [1, 2, 3, 4, 5, 6, 7, 8]),
    ([4, 8, 9, 12, 1, 2, 6, 30], 4, [1, 2, 4, 6, 8, 9, 12, 30]),
    ([], 3, []),
    ([5, 7, 8, 12, 4], 4, [4, 5, 7, 8, 12])
], ids=["width of 1", "width of 2", # "bad test"
        "width of 4", "empty list", "width 4 and incomplete run"])
def test_merge_all_pairs_of_runs(lst, width, expected):
    result = sorting.merge_all_pairs_of_runs(lst, width)
    assert result == expected

@pytest.mark.parametrize("lst, expected", [
    ([], []),
    ([5], [5]),
    ([6, 2, 9, 0, -4, 34893489389, -77], [-77, -4, 0, 2, 6, 9, 34893489389]),
    ([5, 1, 10, 4, 2, 6, 7, 9], [1, 2, 4, 5, 6, 7, 9, 10]),
    (["dog", "cat", "lobster", "elephant", "shark"], ["cat", "dog", "elephant", "lobster", "shark"]),
    ([7, 3, 7, 8, 7, 3, 4, 5, 7], [3, 3, 4, 5, 7, 7, 7, 7, 8]),
    ([3.141233412, 5245.11, 0.2323], [0.2323, 3.141233412, 5245.11])
])
def test_merge_sort(lst, expected):
    result = sorting.merge_sort(lst)
    assert result == expected
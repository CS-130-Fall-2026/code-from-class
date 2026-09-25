"""
test_searching.py
"""

import pytest, searching, copy

@pytest.mark.parametrize("sorted_list, target, expected", [
    ([], 123, None),
    ([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 5, None),
    ([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], 4, 5),
    ([3, 5, 6, 8, 10, 12, 22, 213, 5245423], 3, 0),
    ([3, 5, 6, 8, 10, 12, 22, 213, 5245423], 8, 3),
    ([3, 5, 6, 8, 10, 12, 22, 213, 5245423], 5245423, 8),
    ([3, 5, 6, 8, 10, 12, 22, 213, 5245423], 13, None),
    ([3, 5, 6, 8, 10, 12, 22, 213, 5245423], -6, None),
    ([3, 5, 6, 8, 10, 12, 22, 213, 5245423], 13348234897923, None),
    ([2], 2, 0),
    ([2], 999, None),
    (["apple", "banana", "carrot", "durian", "mangosteen", 'tomato', "vegetable"], "carrot", 2),
    (["apple", "banana", "carrot", "durian", "mangosteen", 'tomato', "vegetable"], "zebra", None),
    ([1.23, 3.52, 7.435], 3.52, 1),
    ([3.52000000000], 3.52, 0),
    ([pytest.approx(0.1 + 0.2), 6.1], 0.30000001, 0)
])
def test_binary_search(sorted_list, target, expected):
    list_copy = copy.deepcopy(sorted_list)
    assert searching.binary_search(sorted_list, target) == expected
    assert list_copy == sorted_list

def test_binary_search_all_elements():
    lst = [2, 34, 55, 123, 787, 32423, 134234, 77777777]
    for i in range(len(lst)):
        assert searching.binary_search(lst, lst[i]) == i

def test_floats():
    assert 0.1 + 0.2 == pytest.approx(0.3)
"""
searching.py
130 Class
Implements binary search
"""

def binary_search(sorted_list, target):
    """Finds target in a sorted list, returning its index. If target is in the
    list multiple times, returns any of their indices. If target isn't
    in sorted_list, returns `None`."""

    start_index = 0
    end_index = len(sorted_list) - 1

    while start_index <= end_index:
        middle_index = (start_index + end_index) // 2

        ## If we've found the target, return the index
        if sorted_list[middle_index] == target:
            return middle_index

        ## If the element in middle is larger than target, only look to middle_index's
        ## left by setting end_index = middle_index - 1
        elif sorted_list[middle_index] > target:
            end_index = middle_index - 1

        ## Otherwise only look to middle_index's right:
        else:
            start_index = middle_index + 1

    return None

def main():
    lst = [3, 5, 6, 8, 14, 22, 28, 29, 30, 31, 32, 33, 89, 91]
    target = 8
    print(f"{target} is in {lst} at index {binary_search(lst, target)}")
    
    target = 7
    print(f"{target} is in {lst} at index {binary_search(lst, target)}")

if __name__ == '__main__':
    main()
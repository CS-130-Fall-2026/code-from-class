"""
sorting.py
130 Class

Implements merge sort for sorting a list.

This file is intended to be a *module* -- a file containing a
function (or class) to be used in other programs.
"""


def merge(left, right):
    """Merges left and right lists, returning a new list."""
    run = []
    indexL = 0
    indexR = 0

    # Continue as long as we aren't to the end of left or right
    while indexL < len(left) and indexR < len(right):
        if left[indexL] <= right[indexR]:
            run.append(left[indexL])
            indexL += 1
        else:
            run.append(right[indexR])
            indexR += 1

    # Only one of these is non-empty. Extending run with both will
    # add that one to the back of run.
    run.extend(left[indexL:])
    run.extend(right[indexR:])

    return run

def merge_all_pairs_of_runs(lst, width):
    """Goes through entire list doing merges of each pair of halves of size `width`."""
    merged_width = width * 2
    new_L = []

    for start in range(0, len(lst), merged_width):
        left = lst[start : start + width]
        right = lst[start + width : start + merged_width]

        merged = merge(left, right)
        new_L.extend(merged)

    return new_L

def merge_sort(lst):
    """Sorts lst using a bottom-up iterative sort."""
    new_L = lst.copy()
    width = 1

    while width < len(lst):
        new_L = merge_all_pairs_of_runs(new_L, width)
        width *= 2

    return new_L

def main():

    l = [6, 2, 9, 0, 11, -3, -1, 7]
    print(merge_sort(l))


# main()

## This says: only run main() if we're calling this file (sorting.py)
## directly using python, not by importing this file
if __name__ == '__main__':
    main()
    
def permutations_of_4_elements():
    """Yield every arrangement of a 4-element list, one at a time."""
    L = ["A", "B", "C", "D"]
    for first in L:
        remaining_after_first = list(L) # Copies L
        remaining_after_first.remove(first)

        for second in remaining_after_first:
            remaining_after_second = list(remaining_after_first)
            remaining_after_second.remove(second)

            for third in remaining_after_second:
                remaining_after_third = list(remaining_after_second)
                remaining_after_third.remove(third)

                for fourth in remaining_after_third:
                    yield [first, second, third, fourth]


def main():
    count = 0
    for perm in permutations_of_4_elements():
        print(perm)
        count += 1
    print("count =", count)

main()
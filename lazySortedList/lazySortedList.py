"""
lazySortedList.py
130 Class
Implements and runs an example of a LazySortedList

This is a "file docstring" and should appear at the top of each file describing
what the file does.
"""

class LazySortedList:
    """A class to store a list that may be sorted, and when sorted is fast
    to search using binary search.
    Attributes:
        _list - list storing the elements of this LSL
        _is_sorted - boolean flag indicating whether the list is still sorted

    This is a Class docstring, and should describe what the class does.
    """

    def __init__(self, init_list = []): ## DO NOT DO THIS, bad things happen
        """The constructor for the class."""
        self._list = init_list # use self. to reference attributes and other methods
        self._is_sorted = True

    def append(self, element):
        """Adds element to the back of our list, and sets the _is_sorted flag
        to False."""
        self._list.append(element)
        self._is_sorted = False

    def __str__(self):
        """Returns a string representation of the object."""
        return "LSL" + str(self._list)


def main():
    fruit = LazySortedList()
    fruit.append("apple")
    fruit.append("strawberry")
    fruit.append("grape")
    fruit.append("orange")

    print(fruit)

    numbers = LazySortedList([7, 2, 29, 11, -4])
    print(numbers)

    veggies = LazySortedList()

    print(veggies)


if __name__ == "__main__":
    main()
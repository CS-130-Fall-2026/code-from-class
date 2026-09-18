"""
lazySortedList.py
130 Class
Implements and runs an example of a LazySortedList

This is a "file docstring" and should appear at the top of each file describing
what the file does.
"""

import sorting, searching, copy

class UnsortedError(Exception):
    """Raised when an operation required sorted order and the list is not sorted.
    Creates our own exception type instead of using a generic one."""

class LazySortedList:
    """A class to store a list that may be sorted, and when sorted is fast
    to search using binary search.
    Attributes:
        _list - list storing the elements of this LSL
        _is_sorted - boolean flag indicating whether the list is still sorted

    This is a Class docstring, and should describe what the class does.
    """

    # def __init__(self, init_list = []): ## DO NOT DO THIS, bad things happen
    def __init__(self, init_list = None):
        """The constructor for the class."""
        if init_list == None:
            self._list = []
            self._is_sorted = True
        else:
            self._list = init_list # use self. to reference attributes and other methods
            self._is_sorted = False # assume passed in list is not sorted

    def append(self, element):
        """Adds element to the back of our list, and sets the _is_sorted flag
        to False."""
        self._list.append(element)
        self._is_sorted = False

    def __str__(self):
        """Returns a string representation of the object.
        Automatically called when you print an object of the class (or
        if you call the str() function on it)"""
        # return "LSL" + str(self._list)
        return f"LSL{self._list}" ## f-string

    def sort(self):
        """Sorts list using merge sort"""
        self._list = sorting.merge_sort(self._list)
        self._is_sorted = True

    def binary_search(self, target):
        """Runs binary search on _list as long as _list is sorted.
        If it isn't, throw an exception!"""

        # if self._is_sorted == False ## Don't write this

        if not self._is_sorted:
            msg = f"""Cannot call binary_search on an unsorted list: {self}
Call sort() method first."""

            ## raise takes an Exception object and throws that exception:
            # raise Exception(msg)
            ## Note: using Exception class is very broad, and makes it so that
            ## try/except will catch all sorts of different errors.
            ## Better: specific Exception class
            ## Best: create our own exception class

            raise UnsortedError(msg)

        return searching.binary_search(self._list, target)

    def __contains__(self, target):
        """Defined to use the `in` operator on LazySortedList. Use binary search,
        and return True if target is in the list, and False otherwise.
        Runs in lgn time"""
        return self.binary_search(target) != None

    def __len__(self):
        """Returns length of this LSL. Called with len() function"""
        return len(self._list)

    def __getitem__(self, index):
        """Returns the elment at the given index.
        Called using square brackets: fruit[3]"""
        return self._list[index]

    def order_statistic(self, k):
        """Returns the kth largest element in the list (0-indexed).
        Ensures that the list is sorted first.
        Runs in constant time"""
        if self._is_sorted:
            return self[k]
        else:
            raise UnsortedError(f"""Cannot call order_statistic on an unsorted list:
{self}
Call sort() first.""")

    def __eq__(self, other):
        """Called using == operator.
        True if self and other have the same list and same sorted status"""
        return self._list == other._list and self._is_sorted == other._is_sorted

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

    print("\n=== Sorting ===")
    fruit.sort()
    numbers.sort()

    print(fruit)
    print(numbers)

    print("\n=== Binary Search ===")
    print(fruit.binary_search("orange"))
    fruit.append("peach")

    ## Throws exception
    # print(fruit.binary_search("orange"))

    ## Handle the exception more gracefully, allowing the program to continue
    ## if we want it to:
    try:
        # a = 5 / 0
        print(fruit.binary_search("orange"))
    # except Exception as error:
        ## Catch exception from Exception class and set error to the error object
    except UnsortedError as error:
        ## This only catches UnsortedErrors, not other exceptions
        print(error)
        fruit.sort()
        print(fruit.binary_search("orange"))

    print("Yay, we made it here")

    print("\n==== in =====")
    if "apple" in fruit:
        print(f"apple is in {fruit}:")
    else:
        print(f"apple is NOT in {fruit}:")

    if "watermelon" in fruit:
        print(f"watermelon is in {fruit}:")
    else:
        print(f"watermelon is NOT in {fruit}:")

    print(f"The length of {fruit} is {len(fruit)}")

    print(fruit[4])

    print(fruit)
    print(fruit.order_statistic(3))
    # fruit.append("mangosteen")
    # print(fruit.order_statistic(3))

    print("\n==== equals =====")
    groceries = LazySortedList(['apple', 'grape', 'orange', 'peach', 'strawberry'])

    print("Is fruit equal to groceries?", fruit == groceries)
    groceries.sort()
    print("Is fruit equal to groceries after sorting?", fruit == groceries)

    ## Aliases

    johns_fruit = fruit
    brents_fruit = copy.deepcopy(fruit)
    print(johns_fruit)
    fruit.append("mangosteen")
    print(johns_fruit)
    print(brents_fruit)

    ## immutable - cannot be changed

    ## list of LSL objects:
    lists = [fruit, numbers, veggies]
    print("----")
    for lst in lists:
        print(lst)

    ## Shallow copy
    other_lists = list(lists)
    lists.append(5)
    print("----")
    for lst in other_lists:
        print(lst)



if __name__ == "__main__":
    main()
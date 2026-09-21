## Assignment with = creates a binding between the variable name and the object.
## For immutable data like ints and strings, this is never a problem. Those
## objects can't change, so it doesn't matter that the variables reference the
## same ones:
a = 5
b = a
a += 10
print(a)
print(b)
# there isn't a method like b.increment()

## We say the two variable names are aliases for the same object.
## If we have aliases of the same mutable object, a change to one variable
## changes the underlying object, and therefore the other variable as well.
zoo = ["Elephant", "Zebra", "Giraffe"]
animals = zoo
zoo[1] = "Lion"
print(zoo)
print(animals) # second element is also "Lion"

## Passing an argument as a parameter uses assignment of parameter names
## to arguments, leading to aliasing:
def append_turtle(lst):
    lst.append("Turtle")

append_turtle(zoo)
print(zoo)
print(animals) # also has "Turtle"

## Python does this to avoid copying large objects/lists, which is time and memory
## intensive. It also allows some functions to mutate on purpose.

## Note: reassigning a variable just changes what object the variable is bound
## to. Therefore reassigning one alias doesn't change the other:
animals = ["Dog", "Cat"]
# animals = ['Elephant', 'Lion', 'Giraffe', 'Turtle']
# animals.append("Frog")
print("reassigning ------")
print(zoo)
print(animals) # now referring to a different object

domestic_animal = ["Cat"]
domestic_animal.append(zoo)
# domestic_animal.extend(zoo)
zoo.remove("Elephant")
print(zoo)
print(domestic_animal)

## Practice: what does this code print?
def mystery(items):
    items.append(4)
    items = [99]

numbers = [1, 2, 3]
mystery(numbers)
print("\n ====== Mystery =====")
print(numbers)

## = creates a binding between a variable and an object

class WeirdNumber:
    def __init__(self, number):
        self.num = number

    def add10(self):
        self.num += 10

    def __str__(self):
        return str(self.num)

    def __repr__(self):
        """Sometimes, Python uses this instead of __str__ when getting a string
        representation. Specifically when it needs a 'computer-readable format'.
        This happens when you print a list, so we need it here."""
        return str(self.num)

nums = [WeirdNumber(5), WeirdNumber(1000), WeirdNumber(77)]
print("\n===== WeirdNumber ======")
print(nums[0])
print(nums)

## The list function makes a shallow copy: different lists, referencing the same
## element objects:
strange = list(nums)
# amir = nums
nums.append(WeirdNumber(12345))
print(nums)
print(strange) # 12345 not appended
# print(amir)

## but, mutating one of the elements changes it in both lists, since they
## reference the same objects:
nums[0].add10()
print(nums)
print(strange) # both have first element changed

## If you actually want to copy everything all the way down, copy.deepcopy:
import copy # usually at the top of the file
total_copy = copy.deepcopy(nums)
total_copy.append(WeirdNumber(-50))
total_copy[1].add10()
print(nums)
print(total_copy)

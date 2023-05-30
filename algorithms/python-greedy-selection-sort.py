"""
selection sort (a type of greedy algorithm)
- sorts a list by selecting the min/max and placing that value at the beginning

1. set first index as min/max
2. iterate through list and compare all values
3. smallest value gets placed at first index
4. reiterate through the list for all other indices until list is sorted

O(n^2)
"""

from typing import List

a = [4, 3, 2, 1, 5]


# always iterates n^2 times
def selectionSort(a: List[int]) -> List[int]:
    for pos in range(len(a)):
        for i in range(pos, len(a)):
            # if current position is smaller than start position, swap values
            if a[i] < a[pos]:
                a[pos], a[i] = a[i], a[pos]

    return a


# doesn't always iterate n^2 times, if minimum index doesn't change, loop breaks
def selectionSort(a: List[int]) -> List[int]:
    for pos in range(len(a)):
        minimum = pos  # keep track of min index
        for i in range(pos, len(a)):
            if a[i] < a[minimum]:
                minimum = i
        # check if min index has changed
        if minimum == pos:
            break
        # if minimum index has changed, beginning index and min index swaps
        else:
            a[pos], a[minimum] = a[minimum], a[pos]

    return a


print(selectionSort(a))

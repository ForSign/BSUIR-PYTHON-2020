#!/usr/bin/env python3
from collections import Counter
import re
from array import *
import numpy as np

print(">>>Hello world!")

# Start
dictor = dict()
print()

with open("TexForLab.txt") as file:
    lines = file.readline()
    # print(lines)
    words = re.sub('[^a-zA-Z ]', '', lines)
    words = words.split()

# 1
dictor.update(Counter(words))
for element in dictor:
    print(element, " was ", dictor.get(element))
else:
    dictor.clear()
    print()

# 2
dictor.update(Counter(words).most_common(10))
print("String: ", end="")
for i in dictor:
    print(str(i).lower(), end=" ")
else:
    print()
    print()


# 3, 4
def getnumbers_stringLike():
    with open("/dev/random", 'rb') as file:
        entering_list = ""
        for i in range(10):
            entering_list += (str(int.from_bytes(file.read(1), 'big')) + " ")
        entering_array = entering_list.split()
        entering_array = list(map(int, entering_array))
        return entering_array


def partition(numb, low, high):
    i = low - 1
    pivot = numb[high]  # warn we take right element as a pivot
    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[j], nums[i] = nums[i], nums[j]
    nums[i+1], nums[high] = nums[high], nums[i+1]
    return i + 1


def quick_sort(numb, low, high):
    if low < high:
        pivot = partition(numb, low, high)
        quick_sort(numb, low, pivot - 1)
        quick_sort(numb, pivot + 1, high)  # pivot at his place?


def merge_sort(numb):
    if len(numb) <= 1:
        return
    middle = len(numb) // 2
    left = numb[:middle]
    right = numb[middle:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            numb[k] = left[i]
            i += 1
            k += 1
        else:
            numb[k] = right[j]
            j += 1
            k += 1

    while i < len(left):
        numb[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        numb[k] = right[j]
        j += 1
        k += 1


nums = getnumbers_stringLike()
print("Quick sort:")
print("#right element taken as a pivot", end="\n\n")
print(nums)
quick_sort(numb=nums, low=0, high=len(nums) - 1)
print(nums, end='\n\n')

nums = getnumbers_stringLike()
print("Merge sort:")
print(nums)
merge_sort(numb=nums)
print(nums)

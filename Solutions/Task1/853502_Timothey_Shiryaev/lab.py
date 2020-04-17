#!/usr/bin/env python3
from collections import Counter
import re
import argparse
from argparse import Namespace
from array import *
import numpy as np

print(">>>Hello world!")

# Start
dictor = dict()
print()


def parsArgs():
    parser = argparse.ArgumentParser(description="Lab1:")
    parser.add_argument("-f", "--file", default="TexForLab.txt", type=open, help="Opens up a file for text read")
    parser.add_argument("-t", "--task", default=None, type=int, help="Opens up a specific task for running")
    parser.add_argument("-c", "--count", default=20, type=int, help="Amount of fibonacci numbers")
    return parser


def fibonacci_generator():
    a,b = 1,1
    yield a
    yield b
    while True:
        a, b = b, a+b
        yield b

# 1
def tsk1():
    dictor.update(Counter(words))
    for element in dictor:
        print(element, " was ", dictor.get(element))
    else:
        dictor.clear()
        print()


# 2
def tsk2():
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
        if numb[j] < pivot:
            i += 1
            numb[j], numb[i] = numb[i], numb[j]
    numb[i+1], numb[high] = numb[high], numb[i+1]
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


def tsk3():
    nums = getnumbers_stringLike()
    print("Quick sort:")
    print("#right element taken as a pivot", end="\n\n")
    print(nums)
    quick_sort(numb=nums, low=0, high=len(nums) - 1)
    print(nums, end='\n\n')


def tsk4():
    nums = getnumbers_stringLike()
    print("Merge sort:")
    print(nums)
    merge_sort(numb=nums)
    print(nums)


def tsk5():
    seq = fibonacci_generator()
    print([next(seq) for _ in range(params.count)])


def choose(argument):
    switcher = {
        1: tsk1,
        2: tsk2,
        3: tsk3,
        4: tsk4,
        5: tsk5,
    }
    switcher.get(argument, lambda: "Invalid month")()

# main
params = parsArgs().parse_args()

if params.file:
    lines = params.file.readline()
    # print(lines)
    words = re.sub('[^a-zA-Z ]', '', lines)
    words = words.split()
else:
    with open("TexForLab.txt") as file:
        lines = file.readline()
        # print(lines)
        words = re.sub('[^a-zA-Z ]', '', lines)
        words = words.split()

if params.task:
    choose(params.task)
else:
    choose(1)
    choose(2)
    choose(3)
    choose(4)
    choose(5)
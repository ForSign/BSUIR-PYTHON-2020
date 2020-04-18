#!/usr/bin/env python3
from collections import Counter
import re
import argparse
import random

# Start
dictor = dict()


def parseargs():
    parser = argparse.ArgumentParser(description="Lab1:")
    parser.add_argument("-f", "--file", default="TexForLab.txt", type=open, help="Opens up a file for text read")
    parser.add_argument("-t", "--task", default=None, type=int, help="Opens up a specific task for running")
    parser.add_argument("-c", "--count", default=10, type=int, help="Amount of fibonacci numbers")
    return parser


params = parseargs().parse_args()


def fibonacci_generator():
    a, b = 1, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


# 1
def count_words_task():
    if params.file:
        lines = params.file.readline()
        words = re.sub('[^a-zA-Z ]', '', lines)
        words = words.split()
    else:
        with open("TexForLab.txt") as file:
            lines = file.readline()
            words = re.sub('[^a-zA-Z ]', '', lines)
            words = words.split()
    print("Count words task")
    dictor.update(Counter(words))
    return dictor


# 2
def most_common_task():
    if params.file:
        lines = params.file.readline()
        words = re.sub('[^a-zA-Z ]', '', lines)
        words = words.split()
    else:
        with open("TexForLab.txt") as file:
            lines = file.readline()
            words = re.sub('[^a-zA-Z ]', '', lines)
            words = words.split()
    print("Most common task")
    dictor.update(Counter(words).most_common(10))
    return dictor


# 3, 4
def get_numbers_string_like():
    with open("/dev/random", 'rb') as file:
        entering_list = ""
        for i in range(10):
            entering_list += (str(int.from_bytes(file.read(1), 'big')) + " ")
        entering_array = entering_list.split()
        entering_array = list(map(int, entering_array))
        return entering_array


def random_pivot(numbs, first, last):
    random_pivote = random.randrange(first, last)
    numbs[first], numbs[random_pivote] = numbs[random_pivote], numbs[first]
    return partition(numbs, first, last)


def partition(numbs, left, right):
    pivot = left
    i = left - 1
    j = right + 1
    while True:
        while True:
            i = i + 1
            if numbs[i] >= numbs[pivot]:
                break
        while True:
            j = j - 1
            if numbs[j] <= numbs[pivot]:
                break
        if i >= j:
            return j
        numbs[i], numbs[j] = numbs[j], numbs[i]


def quick_sort(numb, low, high):
    if low < high:
        pivot = random_pivot(numb, low, high)
        quick_sort(numb, low, pivot - 1)
        quick_sort(numb, pivot + 1, high) # random pivot time taken?


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


def quick_sort_task():
    nums = get_numbers_string_like()
    print("Quick sort:")
    print("#random element taken as a pivot", end="\n\n")
    print(nums)
    quick_sort(numb=nums, low=0, high=len(nums) - 1)
    return nums


def merge_sort_task():
    nums = get_numbers_string_like()
    print("Merge sort:")
    print(nums)
    merge_sort(numb=nums)
    return nums


def fibonacci_task():
    print("Fibonacci task")
    seq = fibonacci_generator()
    return [next(seq) for _ in range(params.count)]


def choose(argument):
    switcher = {
        1: count_words_task,
        2: most_common_task,
        3: quick_sort_task,
        4: merge_sort_task,
        5: fibonacci_task,
    }
    var = switcher.get(argument, lambda: "Invalid data")()
    if params.task == 2:
        print("String: ", end="")
        for i in var:
            print(str(i).lower(), end=" ")
        print()
    else:
        print(var)

# main
if params.task:
    choose(params.task)

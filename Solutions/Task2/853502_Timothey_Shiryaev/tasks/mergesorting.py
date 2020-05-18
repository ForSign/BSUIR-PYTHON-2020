'''
import random

with open('numbers.txt', 'w') as f:
    f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(1000000))
'''
import tempfile
import os
from itertools import islice
#from file to list

def fftl(filename):
    file = open(filename, 'r')
    return list(islice(file, 100000))

def merge_sorting(lis):
    if len(lis) > 1:
        middle = len(lis) // 2
        lp = lis[: middle]
        rp = lis[middle:]
        merge_sorting(lp)
        merge_sorting(rp)
        li, ri = 0, 0
        ti = 0
        while li < len(lp) and ri < len(rp):
            if int(lp[li]) <= int(rp[ri]):
                lis[ti] = lp[li]
                li += 1
            else:
                lis[ti] = rp[ri]
                ri += 1
            ti += 1

        while li < len(lp):
            lis[ti] = lp[li]
            li += 1
            ti += 1

        while ri < len(rp):
            lis[ti] = rp[ri]
            ri += 1
            ti += 1
    return lis

def merge_arrays(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    arr3 = []
    i = 0
    j = 0
    while i < n1 and j < n2:

        if int(arr1[i]) < int(arr2[j]):
            arr3.append(arr1[i])
            i = i + 1
        else:
            arr3.append((arr2[j]))
            j = j + 1

    while  i < n1:
        arr3.append(arr1[i])
        i = i + 1

    while j < n2:
        arr3.append(arr2[j])
        j = j + 1
    return arr3

def external_merge(test):
    tempfiles = []
    file = open(test,'r')
    e = []
    while True:
        temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w')
        e = list(islice(file,100000))
        if not e:
            break
        e = merge_sorting(e)
        temp_file.writelines(e)
        tempfiles.append(temp_file)
        temp_file.flush()
        temp_file.seek(0)

    ans = [merge_arrays(fftl(tempfiles[i].name), fftl(tempfiles[len(tempfiles) - (i + 1)].name)) for i in range(5)]
    ans = [merge_arrays(ans[i], ans[-(i+1)]) for i in range(2)] + [ans[2]]
    ans = [merge_arrays(merge_arrays(ans[0],ans[1]),ans[2])]

    outfile = open('out.txt', 'w')
    outfile.writelines(ans[0])
    outfile.close()

    file.close()

    for i in tempfiles:
        i.close()
        os.remove(i.name)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    a = tuple(map(int, input('Введите элеметы списка: ').split()))
    i = 0
    for index, el in enumerate(a):
        k = a.count(el)
        if k >= 2:
            if len(a) > index + 1:
                if a[index + 1] == el:
                    i = index + 1
                    break
    if i:
        i += 1
        print(a[i:])
    else:
        print("There are no pairs of similar adjacent elements!")

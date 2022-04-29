#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(array1, array2):
    diff = []
    min_val = None
    min_index = None
    max_val = None
    max_index = None
    abs_sum = 0
    index = 0
    for i, j in zip(array1, array2):
        curr_diff = i - j
        diff.append(i - j)
        abs_sum += abs(curr_diff)
        if min_val is None:
            min_val = curr_diff
            min_index = index
            max_val = curr_diff
            max_index = index
        else:
            if curr_diff < min_val:
                min_val = curr_diff
                min_index = index
            if curr_diff > max_val:
                max_val = curr_diff
                max_index = index
        index += 1
    if min_index != max_index and min_val < 0 and max_val > 0:
        array2[min_index], array2[max_index] = array2[max_index], array2[min_index]
        abs_sum = (
            abs_sum
            - abs(diff[min_index])
            - abs(diff[max_index])
            + abs(array1[min_index] - array2[min_index])
            + abs(array1[max_index] - array2[max_index])
        )
    return abs_sum


def main():
    n = int(parse_input())
    array1 = [int(i) for i in parse_input().split()]
    array2 = [int(i) for i in parse_input().split()]
    print(func(array1, array2))


# region fastio

# BUFSIZE = 8192


# class FastIO(IOBase):
#     newlines = 0

#     def __init__(self, file):
#         self._fd = file.fileno()
#         self.buffer = BytesIO()
#         self.writable = "x" in file.mode or "r" not in file.mode
#         self.write = self.buffer.write if self.writable else None

#     def read(self):
#         while True:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             if not b:
#                 break
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines = 0
#         return self.buffer.read()

#     def readline(self):
#         while self.newlines == 0:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             self.newlines = b.count(b"\n") + (not b)
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines -= 1
#         return self.buffer.readline()

#     def flush(self):
#         if self.writable:
#             os.write(self._fd, self.buffer.getvalue())
#             self.buffer.truncate(0), self.buffer.seek(0)


# class IOWrapper(IOBase):
#     def __init__(self, file):
#         self.buffer = FastIO(file)
#         self.flush = self.buffer.flush
#         self.writable = self.buffer.writable
#         self.write = lambda s: self.buffer.write(s.encode("ascii"))
#         self.read = lambda: self.buffer.read().decode("ascii")
#         self.readline = lambda: self.buffer.readline().decode("ascii")


# sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()
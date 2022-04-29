#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(array):
    # print(sorted(array))
    counter = Counter(array)
    array = sorted(counter.keys())
    array = sorted(array)
    curr_min = array[0]
    curr_max = array[-1]
    n = len(array)
    curr_sum = 0
    count = n - 1
    left = 0
    right = n - 1
    while left < right:
        print(curr_sum, curr_max, curr_min)
        if counter[array[left]] * (array[left + 1] - array[left]) - counter[
            array[left]
        ] * (curr_max - curr_min) > counter[array[right]] * (
            array[right] - array[right - 1]
        ) - counter[
            array[right]
        ] * (
            curr_max - curr_min
        ):
            # print(array)
            curr_sum += counter[array[left]] * (curr_max - curr_min)
            left += 1
            curr_min = array[left]
            count -= 1
        else:
            curr_sum += counter[array[right]] * (curr_max - curr_min)
            right -= 1
            curr_max = array[right]
            count -= 1
    return curr_sum


def main():
    result = []
    n = int(parse_input())
    array = [int(i) for i in parse_input().split()]
    result.append(func(array))
    print("\n".join(map(str, result)))


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

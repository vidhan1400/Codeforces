#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(n):
    start_one = True
    ones = []
    twos = []
    for i in range(1, n + 1):
        is_one = start_one
        start_one = not start_one
        for j in range(1, n + 1):
            if is_one:
                ones.append([i, j])
            else:
                twos.append([i, j])
            is_one = not is_one
    one_index = 0
    two_index = 0
    # print(len(ones), len(twos))
    # print(ones, twos)
    for step in range(n ** 2):
        curr = int(parse_input())
        if one_index < len(ones) and two_index < len(twos):
            if curr == 1:
                print(f"2 {twos[two_index][0]} {twos[two_index][1]}\n")
                sys.stdout.flush()
                two_index += 1
            else:
                print(f"1 {ones[one_index][0]} {ones[one_index][1]}\n")
                sys.stdout.flush()
                one_index += 1
        elif one_index == len(ones):
            if step < n ** 2:
                if curr == 2:
                    print(f"3 {twos[two_index][0]} {twos[two_index][1]}\n")
                    sys.stdout.flush()
                else:
                    print(f"2 {twos[two_index][0]} {twos[two_index][1]}\n")
                    sys.stdout.flush()
            else:
                if curr == 2:
                    print(f"3 {twos[two_index][0]} {twos[two_index][1]}")
                    sys.stdout.flush()
                else:
                    print(f"2 {twos[two_index][0]} {twos[two_index][1]}")
                    sys.stdout.flush()
            two_index += 1
        else:
            if step < n ** 2:
                if curr == 1:
                    print(f"3 {ones[one_index][0]} {ones[one_index][1]}\n")
                    sys.stdout.flush()
                else:
                    print(f"1 {ones[one_index][0]} {ones[one_index][1]}\n")
                    sys.stdout.flush()
            else:
                if curr == 1:
                    print(f"3 {ones[one_index][0]} {ones[one_index][1]}")
                    sys.stdout.flush()
                else:
                    print(f"1 {ones[one_index][0]} {ones[one_index][1]}")
                    sys.stdout.flush()
            one_index += 1


def main():
    n = int(parse_input())
    func(n)


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

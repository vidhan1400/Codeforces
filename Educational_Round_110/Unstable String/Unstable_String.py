#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(array):
    num = 0
    last_question = None
    last_number = None
    start = None
    first = None
    first_index = None
    for i, val in enumerate(array):
        # print("Start", i, num, first_index, start, last_question)
        if first is None:
            if val != "?":
                first = val
                first_index = i
                last_question = None
                last_number = i
                if start is None:
                    start = i
            elif last_question is None:
                last_question = i
                start = i
            num += i - start + 1
        else:
            if val == "?":
                num += i - start + 1
                if last_question is None or last_question < last_number:
                    last_question = i
            elif (val == first and (i - first_index) % 2 == 0) or (
                val != first and (i - first_index) % 2 != 0
            ):
                num += i - start + 1
                last_number = i
                last_question = None
            else:
                # num += ((i - start) * (i - start - 1)) // 2
                # print("last")
                if last_question is not None and last_question > first_index:
                    # print("Here")
                    start = last_question
                else:
                    start = i
                    last_question = None
                first_index = i
                first = val
                last_number = i
                num += i - start + 1
        # print(i, val, num, first_index, start, last_question)
    # num += ((len(array) - start) * (len(array) - 1 - start - 1)) // 2
    return num


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        array = parse_input()
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

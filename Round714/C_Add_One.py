#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter

# import sys

# sys.setrecursionlimit(10 ** 9)
CACHES = []
for i in range(10):
    CACHES.append(1)
for i in range(10, 2 * 10 ** 5 + 10):
    CACHES.append((CACHES[i - 9] + CACHES[i - 10]) % (10 ** 9 + 7))


def step(count):
    if CACHES[count] is not None:
        return CACHES[count]
    if count < 10:
        CACHES[count] = 1
        return CACHES[count]
    val = step(count - 9) + step(count - 10)
    # CACHES[count] = val % (10 ** 9 + 7)
    return val % (10 ** 9 + 7)


def func(array):
    n, m = array
    count = 0
    digits = [int(i) for i in str(n)]
    for digit in digits:
        count += step(digit + m) % (10 ** 9 + 7)
    return count % (10 ** 9 + 7)


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        array = [int(i) for i in parse_input().split()]
        result.append(func(array))
    # print(CACHES[3][:10])
    print("\n".join(map(str, result)))


# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()

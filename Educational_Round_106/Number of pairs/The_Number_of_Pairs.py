#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


# def primes(n):
#     r = [False, True] * (n // 2) + [True]
#     r[1], r[2] = False, True
#     for i in range(3, int(1 + n ** 0.5), 2):
#         if r[i]:
#             r[i * i :: 2 * i] = [False] * ((n + 2 * i - 1 - i * i) // (2 * i))
#     return [i for i in range(len(r) - 1) if r[i]]


# PRIMES = primes(10 ** 4)
ALL_DIVS = {}
PRIME_NUMS = [0] * (2 * 10 ** 7 + 1)
for i in range(2, 2 * 10 ** 7 + 1):
    if PRIME_NUMS[i] != 0:
        continue
    for j in range(i, 2 * 10 ** 7 + 1, i):
        PRIME_NUMS[j] += 1


# def primeFactors(n):
#     if n == 1:
#         return set()
#     factors = set()
#     for i in PRIMES:
#         while n % i == 0:
#             n = n // i
#             factors.add(i)
#         if n < i:
#             break
#     if n > 2:
#         factors.add(n)
#     return factors


def printDivisors(n):
    all_div = set()
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            if n == i * i:
                all_div.add(i)
            else:
                all_div.add(i)
                all_div.add(n // i)
        i = i + 1
    return all_div


def func(array):
    count = 0
    c, d, x = array
    g = math.gcd(c, d)
    if x % g != 0:
        return 0
    c, d, x = c // g, d // g, x // g
    if x not in ALL_DIVS:
        ALL_DIVS[x] = printDivisors(x)
    all_div = ALL_DIVS[x]
    for y0 in all_div:
        tmp = y0 + d
        if tmp % c == 0:
            k = tmp // c
            count += 2 ** PRIME_NUMS[k]
    return count


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
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

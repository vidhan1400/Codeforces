import math


def ceil_divisions(num):
    num_index = num
    old_value = num
    pairs = []
    while num > 3:
        next_value = int(math.floor(math.sqrt(num)))
        for value in range(next_value + 1, old_value):
            pairs.append((value, num_index))
        old_value = next_value + 1
        pairs.append((num_index, next_value))
        num = int(math.ceil(num / next_value))
    if old_value > 3:
        pairs.append((3, num_index))
    if num > 2:
        pairs.append((num_index, 2))
    pairs.append((num_index, 2))
    return pairs


if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        num = int(input())
        pairs = ceil_divisions(num)
        print(len(pairs))
        for pair in pairs:
            print(f"{pair[0]} {pair[1]}")

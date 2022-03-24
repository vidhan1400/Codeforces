def painting_the_array_ii(array):
    count = 0
    last1 = None
    last2 = None
    buffer_set = set()
    buffer_last = None
    for i in array:
        if last1 is None:
            last1 = i
            count += 1
        elif i == last1 and not buffer_set:
            pass
        elif last2 is None:
            last2 = i
            count += 1
        elif i == last2 and not buffer_set:
            pass
        elif i == last1:
            count += len(buffer_set)
            last2 = buffer_last
            buffer_set = set()
            buffer_last = None
        elif i == last2:
            count += len(buffer_set)
            last1 = buffer_last
            buffer_set = set()
            buffer_last = None
        elif i in buffer_set and i != buffer_last:
            count += len(buffer_set)
            buffer_set = set()
            buffer_last = None
        elif i in buffer_set and i == buffer_last:
            pass
        else:
            buffer_set.add(i)
            buffer_last = i
    return count + len(buffer_set)


if __name__ == "__main__":
    n = int(input())
    array = [int(i) for i in input().split()]
    print(painting_the_array_ii(array))

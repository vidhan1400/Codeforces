def painting_the_array_i(array):
    count = 0
    last1 = None
    last2 = None
    buffer = None
    buffer_count = 0
    for i in array:
        if last1 is None or (i != last1 and last2 is None):
            last1 = i
            count += 1
        elif last2 is None:
            last2 = i
            count += 1
        elif last1 == last2:
            if i != last1:
                count += 1
            last1 = i
        elif i == last1 and buffer is None:
            last2 = i
            count += 1
        elif i == last2 and buffer is None:
            last1 = i
            count += 1
        else:
            if i == buffer:
                last1 = last2 = i
                count += buffer_count
                count += 1
                buffer = None
                buffer_count = 0
            else:
                buffer = i
                buffer_count += 1
    return count + buffer_count


if __name__ == "__main__":
    n = int(input())
    array = [int(i) for i in input().split()]
    print(painting_the_array_i(array))

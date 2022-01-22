def is_regular_sequence(sequence):
    if len(sequence) % 2 != 0:
        return False
    left = sequence.find("(")
    right = sequence.find(")")
    if left < right:
        return True
    if right == 0 or left == len(sequence) - 1:
        return False
    return True


if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        sequence = input()
        result = is_regular_sequence(sequence)
        if result:
            print("YES")
        else:
            print("NO")

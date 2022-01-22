def max_pre_sum(array):
    max_value = 0
    pre_sum = 0
    for value in array:
        pre_sum += value
        max_value = max(pre_sum, max_value)
    return max_value


def red_and_blue(reds, blues):
    return max_pre_sum(reds) + max_pre_sum(blues)


if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        num_red = int(input())
        reds = [int(i) for i in input().split()]
        num_blue = int(input())
        blues = [int(i) for i in input().split()]
        print(red_and_blue(reds, blues))

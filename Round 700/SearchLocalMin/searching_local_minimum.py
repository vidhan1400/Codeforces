import sys


def searching_local_minimum(lowerbound, upperbound):
    pass


if __name__ == "__main__":
    n = int(input())
    print("? 1")
    sys.stdout.flush()
    lowerbound = int(input())
    lower_index = 1
    print(f"? {n}")
    sys.stdout.flush()
    upperbound = int(input())
    upper_index = n
    for i in range(98):
        middle_index = (lower_index + upper_index) // 2
        print(f"? {middle_index}")
        sys.stdout.flush()
        middle = int(input())
        if lowerbound < upperbound:
            upperbound = middle
            upper_index = middle_index
        else:
            lowerbound = middle
            lower_index = middle_index
        if (upper_index - lower_index) <= 1:
            if lowerbound < upperbound:
                print(f"! {lower_index}")
            else:
                print(f"! {upper_index}")
            break

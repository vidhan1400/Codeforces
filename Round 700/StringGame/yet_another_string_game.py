def replace(letter, index):
    if index % 2 == 0:
        return "a" if letter != "a" else "b"
    return "z" if letter != "z" else "y"


def yet_another_string_game(word):
    return "".join([replace(letter, index) for index, letter in enumerate(word)])


if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        word = input()
        print(yet_another_string_game(word))

from itertools import combinations as comb

letters = ["س", "خ", "ن", "ت"]


# letters = ["ن", "ا", "ی", "ف", "ط", "ص", "م"]
# letters = ["A", "B", "C", "D", "E", "F", "G"]

with open('words.txt', encoding='utf8') as f:
    all_words_1 = f.read().split('\n')

with open('big.txt', encoding='utf8') as f:
    all_words_2 = f.read().split('\n')

with open('distinct_words.txt', encoding='utf8') as f:
    all_words_3 = f.read().split('\n')

all_words = set(all_words_1 + all_words_2 + all_words_3)


def calculate_combinations(str_of_letters, r):
    return ["".join(i) for i in comb(str_of_letters, r)]


def permutation(lst):
    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    res = []
    for i in range(len(lst)):
        m = lst[i]
        rem_lst = lst[:i] + lst[i + 1:]
        for perm in permutation(rem_lst):
            res.append([m] + perm)
    return res


def calc_all_possible_words(list_of_letters, count):
    list_of_words = []
    for i in calculate_combinations("".join(list_of_letters), count):
        for j in i.split(","):
            for p in permutation([x for x in j]):
                list_of_words.append("".join(p))

    for word in set(list_of_words):
        if word in all_words:
            print(word)

    print("number of words: ", len(list_of_words))
    print("number of words without repeat: ", len(set(list_of_words)))


# exp. => calc_all_possible_words(letters, 3)

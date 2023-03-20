import math
from itertools import product
import random


def permutations():
    colour_matrix = []
    c = ["Grey", "Yellow", "Green"]
    for x in product(c, repeat=5):
        colour_matrix.append(x)
    return colour_matrix


def word_entropy(l):
    return l[1]


def word_with_highest_entropy():
    word_matrix = []
    colour_matrix = permutations()
    for x in L:
        medium_entropy = 0
        nr_right_words = [0] * (3 ** 5)
        for z in L:
            result = ()
            for i in range(5):
                if x[i] == z[i]:
                    result += ('Green',)
                else:
                    if z.find(x[i]) != -1:
                        result += ('Yellow',)
                    else:
                        result += ('Grey',)
            nr_right_words[colour_matrix.index(result)] += 1
        for i in range(3 ** 5):
            case = nr_right_words[i] / len(L)
            if case != 0:
                medium_entropy += case * math.log2(1 / case)
        matrix_line = []
        matrix_line.append(x)
        matrix_line.append(medium_entropy)
        word_matrix.append(matrix_line)
        word_matrix.sort(key=word_entropy, reverse=True)
    return (word_matrix[0][0])


def verification(correct_word, optimum_word):
    global L
    result = [0] * 5
    for i in range(5):
        if optimum_word[i] == correct_word[i]:
            result[i] = "Green"
            L = [x for x in L if optimum_word[i] == x[i]]
        elif optimum_word[i] in correct_word:
            result[i] = "Yellow"
            L = [x for x in L if optimum_word[i] in x and optimum_word[i] != x[i]]
        else:
            result[i] = "Grey"
            L = [x for x in L if optimum_word[i] not in x]


L = []
tries_matrix = []


def main():
    global L
    L = open("all_wordle_words.txt", "r").read().strip().split()
    correct = random.choice((open("all_wordle_words.txt", "r")).read().strip().split())
    print(f"The word that should be guessed is: {correct}")
    nr_tries = 0
    optimum_word = word_with_highest_entropy()
    with open("transition.txt", "r+") as f:
        f.write(optimum_word)
    while optimum_word != correct:
        nr_tries += 1
        with open("transition.txt", "r+") as f:
            optimum_word = f.read()
        verification(correct, optimum_word)
        with open("transition.txt", "r+") as f:
            f.write(word_with_highest_entropy())
        print(f"Try number {nr_tries} is: {optimum_word}")
    print("Right answer!")
main()
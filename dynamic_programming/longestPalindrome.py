# https://leetcode.com/problems/longest-palindromic-substring/

def best_solution(string, start, finish, solution_length, solution_string):
    if finish - start > solution_length:
        solution_length = finish-start
        solution_string = string[start:finish+1]
    return solution_length, solution_string


def longest_palindrome(string):
    length = len(string)
    M = [[0] * length for _ in range(length)]
    solution_length = 0
    solution_string = string[0]

    for diagonal in range(length):
        for i, j in zip(range(length), range(diagonal, length)):  # iterate diagonally(only right part)
            if i == j:  # first diagonal is always 1, because it's one character
                M[i][j] = 1
            elif j == i+1:  # second diagonal, no need to look into the rest of the matrix because they are consecutive chars
                if string[i] == string[j]:
                    M[i][j] = 1
                    solution_length, solution_string = best_solution(string, i, j, solution_length, solution_string)
                else:
                    M[i][j] = 0

            else:  # rest of diagonals,
                if string[i] == string[j] and M[i+1][j-1] == 1 :  # look if the inside subtring is a palindrome and check boundaries
                    M[i][j] = 1

                    solution_length, solution_string = best_solution(string, i, j, solution_length, solution_string)
                else:
                    M[i][j] = 0
    return solution_string


print(longest_palindrome("abcda"))

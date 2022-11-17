# Problem What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.

# Solution: Generate all 10! permutations in lexicographic order and select the 1000000th

from itertools import permutations

perms = list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(perms[1000000-1])
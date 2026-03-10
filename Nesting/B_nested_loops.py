#two_dimensional arrays exercise
# Write a function `print2d(matrix)` that accepts a 2D list and prints all inner elements.

def print2d(matrix):
    for row in matrix: #matrix is a 2D list, matrix is a list of lists, so each element in matrix is itself a list, row is each inner list
        for item in row: # row is itself a list, item is each element inside that row.
            print(item)

array1 = [
    ["a", "b", "c", "d"],
    ["e", "f"],
    ["g", "h", "i"]
]

print2d(array1)
# prints:
# a
# b
# c
# d
# e
# f
# g
# h
# i

array2 = [[9, 3, 4], [11], [42, 100]]
print2d(array2)
# prints:
# 9
# 3
# 4
# 11
# 42
# 100


##ake_matrix

# Write a function `make_matrix(m, n, value)` that returns a 2D list of m rows and n columns
# filled with `value`.

def make_matrix(m, n, value):
    return [[value for _ in range(n)] for _ in range(m)] #Outer for _ in range(m) → runs m times → creates rows Inner for _ in range(n) → runs n times → creates columns for each rowvalue → fills every element with the given value,_ → is a throwaway variable because we don’t actually need the index

print(make_matrix(3, 5, None))
print(make_matrix(4, 2, "x"))
print(make_matrix(2, 2, 0))

#3total_product
# Write a function `total_product(matrix)` that returns the product of all numbers in a 2D list.

def total_product(matrix):
    product = 1 # start with 1 because anything multiplied by 1 is itself 
    for row in matrix:
        for num in row:
            product *= num# for each numbber in the current row , multiply it wih product, 
    return product# after all loops finish, product contains the multiplication of all numbers in all rows.

array1 = [[3, 5, 2], [6, 2]]
array2 = [[4, 6], [2, 3], [1, 2]]

print(total_product(array1))  # 360
print(total_product(array2))  # 288

#two_sum pairs
# Write a function `two_sum_pairs(numbers, target)` that returns all unique pairs from
# numbers that sum to target.

def two_sum_pairs(numbers, target):
    pairs = []
    seen = set()# numbers a list of numbers to search, target the sum we are looking for , pairs list that will store all valid pairs, seen a set to keep track of pairs we have already added.
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pair = sorted([numbers[i], numbers[j]]) # sorted.... ensures the smaller number comes first.
                if tuple(pair) not in seen:
                    pairs.append(pair)
                    seen.add(tuple(pair))
    return pairs
#convert to tuple pair,tuples can go in a set, lists cannot , check if we have already seen this if not add it to pairs and seen.

print(two_sum_pairs([2, 3, 4, 6, 5], 8))  # [[2, 6], [3, 5]]
print(two_sum_pairs([10, 7, 4, 5, 2], 12))  # [[10, 2], [7, 5]]
print(two_sum_pairs([3, 9, 8], 11))  # [[3, 8]]
print(two_sum_pairs([3, 9, 8], 10))  # []


# Write a function `zipper(list1, list2)` that returns a 2D list containing pairs of elements at
# the same indices. Assume lists have same length.

def zipper(list1, list2):
    return [[list1[i], list2[i]] for i in range(len(list1))] #use the same index i to pair elements from both lists.

array1 = ["a", "b", "c", "d"]
array2 = [-1, -2, -3, -4]
print(zipper(array1, array2))

array3 = ["whisper", "talk", "shout"]
array4 = ["quiet", "normal", "loud"]
print(zipper(array3, array4))
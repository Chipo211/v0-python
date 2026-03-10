# make_acronym
# Write a function make_acronym(sentence) that accepts a string containing a sentence.
# The function should return a string containing the first character of each word in the sentence.

def make_acronym(sentence):
    words = sentence.split()  # split the sentence into words
    acronym = ""  # empty string to store acronym
    for word in words:  # loop through each word
        acronym += word[0]  # add the first letter
    print(acronym.upper())

make_acronym("New York")  # -> 'NY'
make_acronym("same stuff different day")  # -> 'SSDD'
make_acronym("Laugh out loud")  # -> 'LOL'
make_acronym("don't over think stuff")  # -> 'DOTS'


# reverse_array
# Write a function reverse_array(arr) that accepts a list as an argument.
# The function should return a list containing the elements of the original list in reverse order.

def reverse_array(arr):
    reversed_list = []  # create an empty list
    for i in range(len(arr) - 1, -1, -1):  # loop through each element in reverse
        reversed_list.append(arr[i])
    print(reversed_list)

reverse_array(["zero", "one", "two", "three"])  # -> ['three', 'two', 'one', 'zero']
reverse_array([7, 1, 8])  # -> [8, 1, 7]


# your_average_function
# Write a function your_average_function(numbers) that accepts a list of numbers.
# The function should return the average of all elements in the list.
# If the list is empty, the function should return None.

def your_average_function(numbers):
    if len(numbers) == 0:
        return None
    total_sum = 0  # variable to store the sum
    for num in numbers:
        total_sum += num
    return total_sum / len(numbers)

print(your_average_function([5, 2, 7, 24]))  # -> 9.5
print(your_average_function([100, 6]))  # -> 53
print(your_average_function([31, 32, 40, 12, 33]))  # -> 29.6
print(your_average_function([]))  # -> None


# choose_divisibles
# Write a function choose_divisibles(numbers, target) that accepts a list of numbers and a target number.
# The function should return a new list containing only the elements divisible by the target.

def choose_divisibles(numbers, target):
    divisible_list = []
    for n in numbers:
        if n % target == 0:
            divisible_list.append(n)
    print(divisible_list)

choose_divisibles([40, 7, 22, 20, 24], 4)  # -> [40, 20, 24]
choose_divisibles([9, 33, 8, 17], 3)  # -> [9, 33]
choose_divisibles([4, 25, 1000], 10)  # -> [1000]


# maximum
# Write a function maximum(numbers) that accepts a list of numbers.
# The function should return the largest number in the list.
# If the list is empty, return None.

def maximum(numbers):
    if len(numbers) == 0:  # check if the list is empty
        return None
    max_value = numbers[0]  # start with the first number
    for num in numbers:
        if num > max_value:  # compare current number with max
            max_value = num
    return max_value

print(maximum([5, 6, 3, 7]))  # -> 7
print(maximum([17, 15, 19, 11, 2]))  # -> 19
print(maximum([]))  # -> None


# word_count
# Write a function word_count(sentence, target_words) that accepts a sentence string and a list of target words.
# The function should return a count of how many words in the sentence are also in target_words.

def word_count(sentence, target_words):
    words_list = sentence.split()
    count = 0
    for word in words_list:
        if word in target_words:
            count += 1
    print(count)

word_count("open the window please", ["please", "open", "sorry"])  # -> 2
word_count("drive to the cinema", ["the", "driver"])  # -> 1
word_count("can I have that can", ["can", "I"])  # -> 3

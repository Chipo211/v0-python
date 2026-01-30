#A_arrays_exercise_python
# Write a function `total(numbers)` that accepts a list of numbers as an argument.
# The function should return the sum of all elements in the list.

# Example:

def total(numbers):
    sum = 0 #start the total at 0
    for item in numbers: #goes through the list one number at a time.
        sum = sum + item #adds current number to the running total
    print(sum)
    

total([3, 2, 8]) #-> 13
total([-5, 7, 4, 6]) #-> 12
total([7]) #-> 7
total([]) #-> 0

#stay_positive
# Write a function `stay_positive(numbers)` that accepts a list of numbers.
# The function should return a new list containing only the positive numbers.

# Example:

def stay_positive(numbers):
    new_list = [] #create an empty list, this is where we will store the posisitive numbers
    for item in numbers:
        if item > 0 : #checks if the number is postive
            new_list.append(item)# if positive add to the new list.
    print (new_list)
    
stay_positive([10, -4, 3, 6]) #-> [10, 3, 6]
stay_positive([-5, 11, -40, 30.3, -2]) #-> [11, 30.3]
stay_positive([-11, -30]) #-> []

#Bleep_vowels
# Write a function `bleep_vowels(text)` that accepts a string and returns
# a new string where all vowels (a, e, i, o, u) are replaced with '*'.

# Example:

def bleep_vowels(text):
    new_str = ""
    for ch in text:
        if ch in "aeiou":
            new_str = new_str + "*"
        else:
            new_str = new_str + ch
    print(new_str)
    
    
bleep_vowels("skateboard") #-> 'sk*t*b**rd'
bleep_vowels("slipper") #-> 'sl*pp*r'
bleep_vowels("range") #-> 'r*ng*'
bleep_vowels("brisk morning") #-> 'br*sk m*rn*ng'

#filter_long_words
# Write a function `filter_long_words(words)` that accepts a list of strings.
# The function should return a new list containing only the words that have
# less than 5 characters.

# Example:
def filter_long_words(words):
    new_list = []
    for word in words:
        if len(word) < 5:
            new_list.append(word)
    print(new_list)
    
filter_long_words(["kale", "cat", "retro", "axe", "heirloom"]) #-> ['kale', 'cat', 'axe']
filter_long_words(["disrupt", "pour", "trade", "pic"]) #-> ['pour', 'pic']

#num_odds
# Write a function `num_odds(numbers)` that accepts a list of numbers.
# The function should return the count of odd numbers in the list.

# Example:

def num_odds(numbers):
    count = 0
    for num in numbers:
        if num % 2 != 0: #!= 0 means odd
            count += 1 # increase the counter by 1 when an odd n.o is found
    print(count)
    
    
num_odds([4, 7, 2, 5, 9]) #-> 3
num_odds([11, 31, 58, 99, 21, 60]) #-> 4
num_odds([100, 40, 4]) #-> 0

#strings_to_lengths
# Write a function `strings_to_lengths(strings)` that accepts a list of strings.
# The function should return a new list containing the lengths of each string.

# Example:

def strings_to_lengths(strings):
    lengths = []
    for s in strings:
        lengths.append(len(s))
    return lengths

strings_to_lengths(["belly", "echo", "irony", "pickled"]) #-> [5, 4, 5, 7]
strings_to_lengths(["on", "off", "handmade"]) #-> [2, 3, 8]

#divisors
# Write a function `divisors(num)` that accepts a number.
# The function should return a list containing all positive numbers that divide num exactly.

# Example:
def divisors(num):
    new_list = []
    new_list = []
    for n in range (1, num + 1):
        if num % n == 0:
            new_list.append(n)
    return new_list

divisors(15) #-> [1, 3, 5, 15]
divisors(7) #-> [1, 7]
divisors(24) #-> [1, 2, 3, 4, 6, 8, 12, 24]


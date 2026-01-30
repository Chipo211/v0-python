#make_acronym
# Write a function `make_acronym(sentence)` that accepts a string containing a sentence.
# The function should return a string containing the first character of each word in the sentence.

# Example:
def make_acronym(sentence):
    list = str.split("")
    acronym = ""
    for word in list:
        acronym += word[0]
    print(acronym.upper())

make_acronym("New York") #-> 'NY'
make_acronym("same stuff different day") #-> 'SSDD'
make_acronym("Laugh out loud") #-> 'LOL'
make_acronym("don't over think stuff") #-> 'DOTS'


##return_array

# Write a function `reverse_array(arr)` that accepts a list as an argument.
# The function should return a list containing the elements of the original list in reverse order.

# Example:
def reverse_array(arr):
    new_list = []
    for i in range(len(arr) - 1, -1, -1):
        new_list.append(arr[i])
    print (new_list)
    
reverse_array(["zero", "one", "two", "three"]) #-> ['three', 'two', 'one', 'zero']
reverse_array([7, 1, 8]) #-> [8, 1, 7]


#your_average_function 

# Write a function `your_average_function(numbers)` that accepts a list of numbers.
# The function should return the average of all elements in the list.
# If the list is empty, the function should return None.

# Example:
def your_average_function(numbers):
    if len(numbers) == 0:
        return None
    total = 0
    for num in numbers:
        total += num

    return total / len(numbers)

your_average_function([5, 2, 7, 24]) #-> 9.5
your_average_function([100, 6]) #-> 53
your_average_function([31, 32, 40, 12, 33]) #-> 29.6
your_average_function([]) #-> None

#choose_divisibles
# Write a function `choose_divisibles(numbers, target)` that accepts a list of numbers and a target number.
# The function should return a new list containing only the elements divisible by the target.

# Example:
def choose_divisibles(numbers, target):
    ans_list = []
    for n in numbers:
        if n % target == 0:
            ans_list.append(n)
    print(ans_list)
    
choose_divisibles([40, 7, 22, 20, 24], 4) #-> [40, 20, 24]
choose_divisibles([9, 33, 8, 17], 3) #-> [9, 33]
choose_divisibles([4, 25, 1000], 10) #-> [1000]


#maximum
# Write a function `maximum(numbers)` that accepts a list of numbers.
# The function should return the largest number in the list.
# If the list is empty, return None.

# Example:
def maximum(numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]  # start with the first number
    for num in numbers:
        if num > max_num:
            max_num = num  # update if we find a bigger number
    return max_num

maximum([5, 6, 3, 7]) #-> 7
maximum([17, 15, 19, 11, 2]) #-> 19
maximum([]) #-> None

#word_count

# Write a function `word_count(sentence, target_words)` that accepts a sentence string and a list of target words.
# The function should return a count of how many words in the sentence are also in target_words.

# Example:

def word_count(sentence, target_words):
    words_list = sentence.split()
    count = 0
    for word in words_list:
        if word in target_words:
            count += 1
    print(count)

word_count("open the window please", ["please", "open", "sorry"]) #-> 2
word_count("drive to the cinema", ["the", "driver"]) #-> 1
word_count("can I have that can", ["can", "I"]) #-> 3
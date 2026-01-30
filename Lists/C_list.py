# Write a function `lengthiest_word(sentence)` that accepts a string containing a sentence.
# The function should return the longest word in the sentence.
# If there is a tie, return the word that appears later in the sentence.

# Example:
def lengthiest_word(sentence):
    words = sentence.split()  # split the sentence into words
    if not words:  # handle empty string
        return None
    longest = words[0]
    for word in words:
        if len(word) >= len(longest):  # >= ensures later word wins if tie
            longest = word
    return longest

    
lengthiest_word("I am pretty hungry") #-> 'hungry'
lengthiest_word("we should think outside of the box") #-> 'outside'
lengthiest_word("down the rabbit hole") #-> 'rabbit'
lengthiest_word("simmer down") #-> 'simmer'

##Alternating_caps
# Write a function `alternating_caps(sentence)` that accepts a string containing a sentence.
# The function should return the sentence where words alternate between lowercase and uppercase.

# Example:

def alternating_caps(sentence):
    list_words = sentence.split()
    ans_list = []
    for i in range(len(list_words)):
        if i % 2 == 0:
            ans_list.append(list_words[i].lower())
        else:
            ans_list.append(list_words[i].upper())
    print(ans_list)
    
    
alternating_caps("take them to school") #-> 'take THEM to SCHOOL'
alternating_caps("What did ThEy EAT before?") #-> 'what DID they EAT before?'

#number_range
# Write a function `number_range(min_val, max_val, step)` that accepts three numbers as arguments.
# The function should return a list of numbers starting from min_val to max_val (inclusive),
# incremented by step.

# Example:
def number_range(min_val, max_val, step):
    result = []
    for num in range(min_val, max_val +1, step):
        result.append(num)
    print (result)

number_range(10, 40, 5) #-> [10, 15, 20, 25, 30, 35, 40]
number_range(14, 24, 3) #-> [14, 17, 20, 23]
number_range(8, 35, 6) #-> [8, 14, 20, 26, 32]

#remove_short_words
# Write a function `remove_short_words(sentence)` that accepts a string containing a sentence.
# The function should return a new sentence where all words shorter than 4 characters are removed.

# Example:

def remove_short_words(sentence):
    words = sentence.split()  
    long_words = []
    for word in words:
        if len(word) >= 4:  # keep words with 4 or more letters
            long_words.append(word)
    print(" ".join(long_words)) # join back into a sentence

remove_short_words("knock on the door will you") #-> 'knock door will'
remove_short_words("a terrible plan") #-> 'terrible plan'
remove_short_words("run faster that way") #-> 'faster that'


#3Common_elementsd
# Write a function `common_elements(arr1, arr2)` that accepts two lists as arguments.
# The function should return a new list containing the elements that are found in both input lists.
# The order of elements in the output list doesn't matter.

# Example:
def common_elements(arr1, arr2):
    ans_list = []
    for el in arr1:
        if el in arr2:
            ans_list.append(el)
    print(ans_list)
    
    
common_elements(["a", "c", "d", "b"], ["b", "a", "y"]) #-> ['a', 'b']
common_elements([4, 7], [32, 7, 1, 4]) #-> [4, 7]

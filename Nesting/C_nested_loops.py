# Write a function `remove_dupes(lst)` that accepts a list and returns a new list
# where each element appears only once.

# Example usage:
def remove_dupes(lst):
    result = [] # this will store the new list of unique elements
    seen = set()
    for item in lst:
        if item not in seen:
            result.append(item) #add to result list
            seen.add(item)
    return result

print(remove_dupes(["x", "y", "y", "x", "z"]))  # ['x', 'y', 'z']
print(remove_dupes([False, False, True, False]))  # [False, True]
print(remove_dupes([42, 5, 7, 42, 7, 3, 7, 7]))  # [42, 5, 7, 3]

#REMOVES VOWELS 
# Write a function `remove_vowels(s)` that accepts a string and returns a new string
# with all vowels removed (a, e, i, o, u).

# Example usage:
def remove_vowels(s):
    vowels = "aeiouAEIOU" # define all vowels, include uppercase 
    result = ""
    for char in s:
        if char not in vowels:
            result += char #add none vowel char to result.
    return result

print(remove_vowels("jello"))  # 'jll'
print(remove_vowels("sensitivity"))  # 'snstvty'
print(remove_vowels("cellar door"))  # 'cllr dr'

#SPAM
# Write a function `spam(pairs)` that accepts a 2D list. Each inner list contains
# a word and a number. The function returns a string with each word repeated
# the specified number of times, separated by spaces.

# Example usage:
def spam(pairs):
    result = [] # store all repeated words
    for word, count in pairs:
        result.extend([word]* count) #repeat the word 'count' times and add to result 
    return "".join(result) #join all words with spaces into a single string
    
array1 = [["hi", 3], ["bye", 2]]
print(spam(array1))  # 'hi hi hi bye bye'

array2 = [["cat", 1], ["dog", 2], ["bird", 4]]
print(spam(array2))  # 'cat dog dog bird bird bird bird'

#REMOVE IRST VOWEL 
# Write a function `remove_first_vowel(s)` that accepts a string and returns the string
# with its first vowel removed.

# Example usage:
def remove_first_vowel(s):
    vowels = "aeiouAEIOU"
    for i, char in enumerate(s): # gives both the index i & char
        if char in vowels:
            return s[:i] + s[i+1:] #remove the first vowel,s[:i] → substring from start up to (but not including) the vowels[i+1:] → substring from after the vowel to the end
    return s 

print(remove_first_vowel("volcano"))  # 'vlcano'
print(remove_first_vowel("celery"))  # 'clery'
print(remove_first_vowel("juice"))  # 'jice'

#SHORTEN LONG WRDS
# Write a function `shorten_long_words(sentence)` that accepts a string and returns
# the same sentence where words longer than 4 characters have their vowels removed.

# Example usage:
def shorten_long_words(sentence):
    vowels = "aeiouAEIOU"
    words = sentence.split()  # split the sentence into words
    new_words = []

    for word in words:
        # Check if the word length is greater than 4
        if len(word) > 4:
            # Remove vowels from the word
            new_word = "".join([char for char in word if char not in vowels])
            new_words.append(new_word)
        else:
            # Keep the word as-is
            new_words.append(word)
    
    # Join the words back into a sentence
    return " ".join(new_words)

print(shorten_long_words("they are very noble people"))  # 'they are very nbl ppl'
print(shorten_long_words("stick with it"))  # 'stck with it'
print(shorten_long_words("ballerina, you must have seen her"))  # 'bllrna, you must have seen her'

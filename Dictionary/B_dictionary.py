#Character count
def character_count(s):
    counts = {}  #create an empty dictionary
    for char in s: #loop through each character in the string
        if char in counts: #checks if the character is already in the  dictionary, yes add 1, no set count to 1
            counts[char] += 1 # increase the count if char already exists
        else:
            counts[char] = 1 #initialize the count to 1 if chracter is new 
    return counts

print(character_count("evening"))
# { 'e': 2, 'v': 1, 'n': 2, 'i': 1, 'g': 1 }

print(character_count("mississippi"))
# { 'm': 1, 'i': 4, 's': 4, 'p': 2 }

print(character_count("chili"))
# { 'c': 1, 'h': 1, 'i': 2, 'l': 1 }

#Letter_map

def letter_map(s, mapping):
    new_string = "" #start with an empty string
    for char in s:
        if char in mapping:
            new_string += mapping[char]  # Replace with mapped value
        else:
            new_string += char           # Keep original if not in mapping
    return new_string

print(letter_map("symbolic", {"y":"i","o":"a","c":"k" }))
# 'simbalik'

print(letter_map("colossal", {"o":"x","s":"p" }))
# 'cxlxppal'

print(letter_map("miniscule", {"u":"t","i":"f","e":"q" }))
# 'mfnfsctlq'

#most commoe letter

def most_common_letter(s):
    counts = {}  
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    most_common = max(counts, key=counts.get) #ind the character with the maximum count 
    return most_common

print(most_common_letter("building"))
# 'i'

print(most_common_letter("shoestring"))
# 's'

print(most_common_letter("preparedness"))
# 'e'

#word replacement

def word_replace(sentence, mapping):
    words = sentence.split()  # Split sentence into words
    new_words = []
    
    for word in words:
        if word in mapping:
            new_words.append(mapping[word])  # Replace word if in dictionary
        else:
            new_words.append(word)           # Keep original word if not in dictionary
    
    return " ".join(new_words)  # Join words back into a sentence

print(word_replace(
"I never take naps during the day",
    {"never":"always","day":"weekend" }
))
# 'I always take naps during the weekend'

print(word_replace(
"the park is closed",
    {"closed":"open","the":"a" }
))
# 'a park is open'

print(word_replace(
"I do what I want",
    {"I":"we","cat":"dog" }
))
# 'we do what we want'

#avergare age
def get_average_age(people):
    total_age = 0
    for person in people:
        total_age += person["age"]  # Add each person's age
    average = total_age / len(people)  # Divide by the number of people
    return round(average, 2)  # Round to 2 decimal places

peeps = [
    {"name":"Lovelace","age":36,"born":"London, UK" },
    {"name":"Kleene","age":85,"born":"Connecticut, US" },
    {"name":"Turing","age":41,"born":"London, UK" },
    {"name":"Hopper","age":85,"born":"New York, US" },
]

print(get_average_age(peeps))
# 61.75


people = [
    {"name":"Orwell","age":46,"born":"Bihar, India" },
    {"name":"Bradbury","age":91,"born":"California, US" },
    {"name":"Huxley","age":69,"born":"California, US" },
]

print(get_average_age(people))
# 68.67
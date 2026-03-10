#snippet.1
# Predict what this will print:
for i in range(1, 5): 
    for j in range(1, 4):
        print(i, j)
#So for every single i, j goes from 1 to 3
#snippet 2

for n in range(2): #means start at 0 and top before 2 ; n = 0, 1
    print("n=" + str(n)) # n is 0, str(n) converts number into a string ; n=0
    for m in range(5):#inner loop: 0-4
        print("   m=" + str(m)) # spaces before m are just indentation to make it look neat, ;m=0...
    print("n=" + str(n)) # after the inner loop ends , n is still 0 it hasnt changed.  so it prints again n=0 


#snippet 3
friends = ["philip", "abby", "phelipe", "simcha"]

for i in range(len(friends)):# len(friends) = 4,  range(4)
    for j in range(len(friends)): #range(4); 0,1,2,3
        print(friends[i], friends[j])


#snippet 4
locations = ["flatbush", "williamsburg", "bushwick", "greenpoint"]

for i in range(len(locations)): #ramge(4)
    for j in range(i + 1, len(locations)): # range (i + 1, 4), so intsead of starting from 0 its going to start from i + 1, it skips prev combinations & avoids duplicates & skips itself 
        print(locations[i], locations[j])


#snippet 5
colors = ["red", "purple", "orange"]

for color_str in colors: # take all the words and store then in color_str
    print(color_str)
    for char in color_str: # when you loop over a string in python, it automaticaly loops over each character.
        print(char)# so red , becomes r e d




#pair_priint
# Write a function `pair_print(arr)` that accepts a list and prints all unique pairs
# of elements in the list. It doesn't need to return anything.

# Example:
def pair_print(arr):
    # Loop through each element except the last
    for i in range(len(arr)): # moves through every element.
        for j in range(i + 1, len(arr)):
            print(f"{arr[i]} - {arr[j]}")


pair_print(["artichoke", "broccoli", "carrot", "daikon"])
# prints
# artichoke - broccoli
# artichoke - carrot
# artichoke - daikon
# broccoli - carrot
# broccoli - daikon
# carrot - daikon

#EXAMPLE 2
#print_combinations
# Write a function `print_combinations(arr1, arr2)` that accepts two lists.
# The function should print all combinations taking one element from the first list
# and one from the second list. It doesn't need to return anything.

# Example:

def print_combinations(arr1, arr2):
    for item1 in arr1: # go throught the 1st list and take 1 element at a time and stor it in item1
        for item2 in arr2:
            print(f"{item1} {item2}") # what happens now is that for each item in list 1, pair it with every item in list 2. f means formatted string,

colors = ["gray", "cream", "cyan"]
clothes = ["shirt", "flannel"]
print_combinations(colors, clothes)
# prints:
# gray shirt
# gray flannel
# cream shirt
# cream flannel
# cyan shirt
# cyan flannel

#EXAMPLE 3
#Two_sum
# Write a function `two_sum(numbers, target)` that accepts a list of numbers and a target number.
# The function should return True if there exists a pair of distinct elements in the list that sum to the target.
# Otherwise, return False.

# Example:

def two_sum(numbers, target):
    seen = set()  # set(),To store numbers we have seen, only keeps unique elements.
    for num in numbers:# go through every numberr in the list, 1 by 1
        if target - num in seen:
            return True #target-num is the number we need to reach the target sum with the current  number.
        seen.add(num)
    return False

two_sum([2, 3, 5, 9], 7) #-> True
two_sum([2, 3, 5, 9], 4) #-> False
two_sum([6, 3, 4], 10) #-> True
two_sum([6, 5, 1], 10) #-> False

def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return True
    return False


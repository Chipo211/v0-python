#one_to_four
# Write a function `one_to_four` that prints the numbers 1 through 4 (inclusive).

def one_to_four():
    for i in range(1,5):
        print(i)
    
one_to_four()

#count_up
# Write a function `count_up(max_num)` that prints numbers from 1 to max_num.
def count_up(max_num):
    for i in range(1, max_num):
        print(i)

count_up(5)
count_up(3)

#min_to_max
# Write a function `min_to_max(min_num, max_num)` that prints all numbers from min to max inclusive.


def min_to_max(min_num, max_num):
    for i in range (min_num, max_num + 1):
        print(i)
        
min_to_max(5, 9)
min_to_max(11, 13)
min_to_max(20, 11)   # what happens here?

#string_iterate
# Write a function `string_iterate(text)` that prints each character of the string.

def string_iterate(text):
    for char in text:
        print(char)

string_iterate("celery")
string_iterate("hat")

#Evens
# Write a function `evens(max_num)` that prints all positive even numbers LESS than max_num.

def evens(max_num):
    for num in range(2, max_num, 2):# start at the first positive even n.o, max_num stop before this number, step by 2 each time, so we only get even numbers.
        print(num)
    
evens(11)
evens(8)

#aternative way 
def evens(num):
    for i in range(1, num):
        if i % 2 == 0:
            print(i)

evens(11)
evens(8)

#BONUS CHALLNGE
#sum_of_range
def sum_of_range(n):
    total = 0 # start with 0
    for i in range(1, n+1): # numbers from 1 to n inclusive
          total += i # add i to total each time
    print(total)  #print the final total
    
         
sum_of_range(5) #0+1=1,1+2=3,3+3=6,6+4=10,10+5=15;
# prints: 15

#countdown

def countdown(n):
    for i in range(n, 0, -1): #n start at this number, 0 stop before 0, -1 count backwards by 1.
        print(i)
        
countdown(5)
# 5
# 4
# 3
# 2
# 1

#find_char

def find_char_positions(word, char):
    for i in range(len(word)):
        if word[i] == char: #check if the charactr matches
            print(i)
            
find_char_positions("banana", "a")
# 1
# 3
# 5

#multiplication

def multiplication_table(n):
    for i in range(1,11): #numbers from 1 to 10
        print(n * i)
    
multiplication_table(4)
# 4
# 8
# 12
# ...
# 40




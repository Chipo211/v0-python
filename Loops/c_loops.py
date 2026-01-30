#divisible_range
# Write a function `divisible_range(min_val, max_val, num)` that prints all numbers
# between min_val and max_val (exclusive) that are divisible by num.
# The function does not return a value, just prints.

# Example:
def divisible_range(min_val, max_val, num):
    for i in range(min_val + 1, max_val):
        print(i)
      
    
divisible_range(17, 40, 9)
# 18
# 27
# 36

divisible_range(10, 24, 4)
# 12
# 16
# 20

#reverse_iterate
# Write a function `reverse_iterate(text)` that prints each character of the string
# in reverse order. The function does not return a value, just prints.

# Example:
def reverse_iterate(text):
    for i in range(len(text) - 1, -1, -1): #len(text)-1 starts at the last index, -1 stops before index -1(so index 0 is included), -1(step) moves backwards, text[i]- prints one character at a time.
        print(text[i])
        
reverse_iterate("carrot")
# t
# o
# r
# r
# a
# c

reverse_iterate("box")
# x
# o
# b

#remove_capitals
# Write a function `remove_capitals(text)` that returns a new string with all
# capital letters removed.

# Example:

def remove_capitals(text):
    ans = ""
    for ch in text: #loops through the string one character at a time.
        if ch.lower() == ch: #converts the character to lower case
            ans = ans + ch # adds the allowed character to ans
    return(ans)# returnn lets the value to be used later, printing only displays 
    
remove_capitals("fOrEver")     #-> 'frver'
remove_capitals("raiNCoat")    #-> 'raioat'
remove_capitals("cElLAr Door") #-> 'clr oor'

#raise_power
# Write a function `raise_power(base, exponent)` that returns the result of
# base raised to the exponent using loops (do not use ** operator or math.pow).

# Example:
def raise_power(base, exponent):
    result = 1 # start with1 because anything to power 0 is 1
    for _ in range(exponent): #_ is a placeholder variable since we don’t need the actual number, just want to repeat
        result = result * base
    return result

raise_power(2, 5)  #-> 32
raise_power(4, 3)  #-> 64
raise_power(10, 4) #-> 10000
raise_power(7, 2)  #-> 49

#censor
# Write a function `censor_e(text)` that returns a new string where all 'e' characters
# are replaced with '*'.

# Example:
def censor_e(text):
    result = ""
    for ch in text: #looks at each char in the string
        if ch == "e": 
            result += "*" # replace it with *
        else:
            result += ch #otherwise, keep the character
    return result #return the final string

censor_e("speedy")  #-> 'sp**dy'
censor_e("pending") #-> 'p*nding'
censor_e("scene")   #-> 'sc*n*'
censor_e("heat")    #-> 'h*at'

#fizz_buzz
# Write a function `fizz_buzz(max_num)` that prints all numbers <= max_num
# that are divisible by 3 or 5 but not both.
# The function does not return a value, just prints.

# Example:
def fizz_buzz(max_num):
    for i in range(1, max_num + 1):
        if i % 3 or i % 5:
            print(i)
            
fizz_buzz(18)
# 3
# 5
# 6
# 9
# 10
# 12
# 18

fizz_buzz(33)
# 3
# 5
# 6
# 9
# 10
# 12
# 18
# 20
# 21
# 24
# 25
# 27
# 33
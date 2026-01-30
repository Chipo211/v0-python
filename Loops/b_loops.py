#five_multiples
# Write a function `five_multiples_of(n)` that prints the first five multiples of n.
# The function does not return a value, just prints.

# Example:
def five_multiples_of(num):
    for n in range(1,6):
        print(n * num)
        
five_multiples_of(7)

# 7
# 14
# 21
# 28
# 35

#sum_up_to
# Write a function `sum_up_to(max_num)` that returns the sum of all whole numbers
# from 1 to max_num inclusive.

# Example:
def sum_up_to(n):
    total = 0
    for i in range(1, n+1):
        total = total + i
    return total
    
sum_up_to(4)  #-> 10
sum_up_to(5)  #-> 15
sum_up_to(2)  #-> 3

#no_ohs
# Write a function `no_ohs(text)` that prints each character of the string except 'o'.
# The function does not return a value, just prints.

# Example:

def no_ohs(text):
    for ch in text:
        if ch != 'o':
            print(ch)
    
no_ohs("code")
# c
# d
# e

## Write a function `odd_sum(max_num)` that returns the sum of all odd numbers
# from 1 to max_num inclusive.

# Example:

def odd_sum(max_num):
    total = 0
    for n in range (1, max_num + 1):
        if n % 2 != 0 :
         total += n
    return total
    
odd_sum(10) #-> 25  # 1 + 3 + 5 + 7 + 9
odd_sum(5)  #-> 9   # 1 + 3 + 5

#string_repeater

# Write a function `string_repeater(text, n)` that returns a new string
# consisting of `text` repeated `n` times.

# Example:
def string_repeater(text, n):
    ans_str = ""
    for i in range(n):
        ans_str = ans_str + text
    print (ans_str)
    
string_repeater("q", 4)  #-> 'qqqq'
string_repeater("go", 2) #-> 'gogo'
string_repeater("tac", 3) #-> 'tactactac'


#product_up
# Write a function `product_up_to(max_num)` that returns the product of all numbers
# from 1 to max_num inclusive. (1*2*3*...*max_num)

# Example:
def product_up_to(max_num):
    product = 1  #start at 1 because multiplying by 0 would give 0
    for i in range (1, max_num + 1):
        product *= i #same as (product = product * i)
    return product

product_up_to(4) #-> 24
product_up_to(5) #-> 120
product_up_to(7) #-> 5040

#div_by_either
# Write a function `div_by_either(num1, num2, max_num)` that prints all positive numbers
# less than max_num that are divisible by num1 or num2.
# The function does not return a value, just prints.

# Example:

def div_by_either(num1, num2, max_num):
    for i in range (1, max_num): #goes through all positiive numbers less than maax_num
        if i % num1 == 0 or i % num2 == 0:#checks if i is divisible by num1/num2, or = either condition iis enough
            print(i)
            
div_by_either(4, 3, 16)
# 3
# 4
# 6
# 8
# 9
# 12
# 15


def get_price():
    return 10

print(get_price())   # You pressed the button
print(get_price)  #If you dont press the button. 

#is_div_by_4
# Write a function `is_div_by_4` that accepts a number as an argument.
# The function should return a boolean indicating whether or not
# the number is divisible by 4.
def is_div_by_4(num): 
    return num % 4 == 0
print(is_div_by_4(8))   # True
print(is_div_by_4(12))  # True
print(is_div_by_4(24))  # True
print(is_div_by_4(9))   # False
print(is_div_by_4(10))  # False


#keep_it_quiet
# Write a function `keep_it_quiet` that accepts a string as an argument.
# The function should return the lowercase version of the string
# with 3 periods added to the end.
def keep_it_quiet(s):
    return s.lower() + "..."

print(keep_it_quiet("HOORAY"))     # "hooray..."
print(keep_it_quiet("Doggo"))      # "doggo..."
print(keep_it_quiet("WHAT?!?!"))   # "what?!?!..."

#is_long
# Write a function `is_long` that accepts a string as an argument.
# The function should return a boolean indicating whether the string
# is longer than 5 characters.

def is_long(s):
    return len(s) > 5

print(is_long("pie"))         # False
print(is_long("kite"))        # False
print(is_long("kitty"))       # False
print(is_long("telescope"))   # True
print(is_long("thermometer")) # True
print(is_long("restaurant"))  # True

#half
# Write a function `half` that accepts a number as an argument.
# The function should return half of the number.

def half(num):
    return num/2

print(half(8))    # 4
print(half(15))   # 7.5
print(half(90))   # 45

#ends_with_t
# Write a function `ends_with_t` that accepts a string as an argument.
# The function should return a boolean indicating whether the string
# ends with the character "t".

def ends_with_t(s):
    last_char = s[-1]
    if last_char == 't':
        return True
    else:
        return False

print(ends_with_t("smart"))      # True
print(ends_with_t("racket"))     # True
print(ends_with_t("taco"))       # False
print(ends_with_t("boomerang"))  # False

#Alternative way 
def ends_with_t(s):
    return s[-1] == "t"

#average.py
# Write a function `average` that accepts three numbers as arguments.
# The function should return the average of the three numbers.

def average(n1, n2, n3):
    return (n1 + n2 + n3)/3

print(average(3, 10, 8))    # 7
print(average(10, 5, 12))   # 9
print(average(6, 20, 40))   # 22




#E.g 1

print("start")

for i in range(5):
    print(i)
    
print("end")


print("hello")

for i in range(5): # range(5) creates a sequence of numbers, 0,1,2,3,4, the loop runs 5 times (once for each number), i stores the current number each time. in this case we do not use i but code.
    print("code") # prints code 5 times

print("goodbye")
print("*********")

#Snippet_1.py
print("hi")

for i in range(3, 8): ##starts at 3 stops before 8,  so the values of i will be 3,4,5,6,7
    print("program")# inside the loop each time the loop runs "program is printed" 
    print(i)#the current value of i is printed. e.g program - 3 - program - 4

print("bye")# runs after the loop finishes

#snippet_3
def foo():
    for num in range(10, 0, -2): #start at 10, stop before 0, count backwards by 2, 
        print(num)#prints 10,8,6,4,2

print("begin") #prints begin
foo() #now the function acrtually runs.
print("end")
foo() # the function runs again and prints the same numbers again

#snippet 4
word = "street" # stores the string street

for i in range(len(word)): #len(word) is 6 bccx street has 6 letters - range(6) produces = 0,1,2,3,4,5
    print(i) #i is the index, word[i] gets the character at that index
    print(word[i])# i=0 - s, 1-t..
    # other ways to do it could be word ="street", for index, letter in enumerate(word):,  print(index, letter)

#snippet 5
total = 0 # this will running sunm(meaning a total that keeps increasing step by step as the program runs.)
# think of total as a bucket that u keep adding numbers into.
for i in range(1, 5):
    total += i # total =total+1 , total =0+1,total=total +2 - 3,
    print(total)

print("grand total:", total)
#A running sum is a variable that remembers the total so far and keeps growing as the loop continues.


#SNIPPET 1
movie = {
"title":"Fight Club",
"year":1999,
"genre": ["drama","thriller"],
"starring": ["Brad Pitt","Edward Norton"],
}

print(movie["year"])
print(movie["title"])
print(movie["genre"])
print(movie["genre"][0]) #first element
print(movie["genre"][1]) #second element

print(movie.get("duration"))# duration does not exist in the dictionary, .get() safely returns none instead o crashing
print(movie["starring"][1])
print(len(movie["starring"]))

#Snippet 2
restaurant = {
"name":"Bob's Burgers",
"location":"123 Ocean Avenue",
"owners": ["Bob Belcher","Linda Belcher"],
"established":2011,
"menu": ["burgers","fries","shakes"],
}

print("owners"in restaurant) #checks if owners is a key in the dictionary.
print("employees"in restaurant) #employees is not a key so false (in checks keys not values)

some_key ="menu"
print(some_key in restaurant)

print(restaurant["menu"])
print(restaurant.get("menu"))
print(restaurant[some_key])
print(restaurant.get("some_key"))#some_key is made as a single string, so its false cause its not a key in the dictionary

print("fries"in restaurant["menu"])

#snippet 3
dog = {
"name":"Manny",
"age":5,
"breed":"pug",
"color":"fawn",
"favoriteFoods": ["bacon"],
}

print(dog["age"])
print(dog["breed"])
print(dog["favoriteFoods"])

dog["age"] +=1
dog["breed"] = dog["breed"].upper()
dog["favoriteFoods"].append("sausage") # adds sausage to the list

print(dog["age"])
print(dog["breed"])
print(dog["favoriteFoods"])

for key in dog: # go through every key inside the dictionay
    print(key,"is", dog[key])

#snippet 4
recipe = {
"name":"Old Fashioned Pancakes",
"difficulty":"easy",
"tasty":True,
"ingredients": ["eggs","milk","butter","flour","sugar"],
}

print(recipe["name"])
print(recipe["name"])
print(len(recipe["ingredients"]))
print(recipe.get("calories"))

some_variable ="difficulty"
print(recipe[some_variable])
print(recipe.get("some_variable"))

for ingredient in recipe["ingredients"]:
    print(ingredient)


#email parse

def email_parse(email):
    parts = email.split("@")
    
    return { 
            "username": parts[0],
            "domain": parts[1]
            }
    
print(email_parse("coolcoder42@goodmail.com"))
# { 'username': 'coolcoder42', 'domain': 'goodmail.com' }

print(email_parse("az@woohoomail.com"))
# { 'username': 'az', 'domain': 'woohoomail.com' }

print(email_parse("1337pr0graMmer@coldmail.edu"))
# { 'username': '1337pr0graMmer', 'domain': 'coldmail.edu' }

#key Pair

def key_pair(dict1, dict2, key):
    return [dict1[key], dict2[key]]

cat1 = {"name":"jinkee","breed":"calico" }
cat2 = {"name":"garfield","breed":"red tabby" }

print(key_pair(cat1, cat2,"breed"))
# ['calico', 'red tabby']

print(key_pair(cat1, cat2,"name"))
# ['jinkee', 'garfield']

#element_quantities 
def element_quantities(quantities):
    result = [] #empty list this is where we will store the repeated elements.
    
    for element in quantities:
        amount = quantities[element]
        result.extend([element] * amount)#. extend() adds multiple items into the list.
        
    return result

quantities1 = {"cat":3,"bird":1,"dog":2 }
print(element_quantities(quantities1))
# ['cat', 'cat', 'cat', 'bird', 'dog', 'dog']

quantities2 = {"blue":3,"brown":1 }
print(element_quantities(quantities2))
# ['blue', 'blue', 'blue', 'brown']


#max_object value

def max_object_value(dict):
    max_key =max (dict, key=dict.get)# find the key whose value is the largest
    return[max_key, dict[max_key]]

print(max_object_value({"a":5,"b":2,"c":6,"d":7,"e":4 }))
# ['d', 7]

print(max_object_value({"lychee":11,"rambutan":13,"papaya":9 }))
# ['rambutan', 13]
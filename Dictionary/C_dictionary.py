#Greatest_population

def greatest_population(countries):
    largest_country = countries[0]  # Start by assuming the first country is the largest
    
    for country in countries:
        if country["population"] > largest_country["population"]:
            largest_country = country  # Update if we find a bigger population
    
    return largest_country["name"]  # Return the name of the country

countries1 = [
    {"name":"Cameroon","population":27744989,"gdp":38.68 },
    {"name":"Belarus","population":9477918,"gdp":59.66 },
    {"name":"Indonesia","population":267026366,"gdp":1042 },
    {"name":"Guyana","population":750204,"gdp":3.88 },
]

print(greatest_population(countries1))
# 'Indonesia'


countries2 = [
    {"name":"New Zealand","population":4925477,"gdp":204.9 },
    {"name":"Mozambique","population":30098197,"gdp":14.72 },
    {"name":"Greenland","population":57616,"gdp":2.71 },
    {"name":"Kazakhstan","population":19091949,"gdp":179.3 },
    {"name":"Burma","population":56590071,"gdp":71.21 },
]

print(greatest_population(countries2))
# 'Burma'

#Pluck

def pluck(dict, keys):
    new_dict = {}
    
    for key in keys:
        if key in dict: #does this key exist in the original dictionary
            new_dict[key] = dict[key]#if the key exists take the value from the original dict and put it inside the new dict
    
    return new_dict

print(pluck(
    {"name":"Fido","color":"Brown","breed":"German Shepherd" },
    ["name","breed"]
))
# { "name": "Fido", "breed": "German Shepherd" }

print(pluck(
    {"make":"Tesla","mpg":93,"model":"Model X","color":"white" },
    ["make","model"]
))
# { "make": "Tesla", "model": "Model X" }

#Object_Add

def object_add(dict1, dict2):
    # create a new empty dictionary to store the result
    result = {}
    
    # loop through the first dictionary
    for key in dict1:
        if key in dict2:  # key exists in both dictionaries
            result[key] = dict1[key] + dict2[key]  # sum the values
        else:  # key exists only in dict1
            result[key] = dict1[key]  # keep as-is
    
    # loop through the second dictionary to find keys not in the first
    for key in dict2:
        if key not in result:  # key was only in dict2
            result[key] = dict2[key]
    
    # return the final merged dictionary
    return result

obj1 = {"x":3,"y":10 }
obj2 = {"y":2,"x":1 }

print(object_add(obj1, obj2))
# { "x": 4, "y": 12 }


obj3 = {"a":3,"b":2,"c": -1 }
obj4 = {"b":5,"c":1,"e":4 }

print(object_add(obj3, obj4))
# { "a": 3, "b": 7, "c": 0, "e": 4 }

#Secret_Cipher
def secret_cipher(text, cipher_map):
    # create an empty string to store the result
    result = ""
    
    for char in text:
        if char in cipher_map:
            # if character exists in cipher map, add its mapped value
            result += cipher_map[char]
        else:
            # if character does not exist, add "?"
            result += "?"
    
    # return the final ciphered string
    return result

print(secret_cipher("jello", {"j":"r","l":"s","e":"i" }))
# 'riss?'

print(secret_cipher("lantern", {"e":"o","l":"p","n":"m","r":"j" }))
# 'p?m?ojm'

myDictionary = {"username": "LoginUser", "password": "1234"}

print(myDictionary)
print(myDictionary["password"])

yourDictionary = {"k1": 100, "k2": [1,2,3,4,"selam"], "k3": {"insideKey": 100 }}

print(yourDictionary["k3"]["insideKey"])

asdf ={"k1":[1,2,3]}

print(yourDictionary["k2"][4].upper())

#adding a new key-value to a dictionary

asdf["k2"]= ["a","b"]

print(asdf)

#changing/assiging new value to an existing key-value pair

asdf["k1"] = ["new value"]
print(asdf)

#get all the keys

print(asdf.keys())

#get all the values

print(asdf.values())

#get them in pairs

print(asdf.items())
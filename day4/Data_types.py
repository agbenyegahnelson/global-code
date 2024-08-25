# String data types

# Literal assignment
name = "Nelson Joel"
surname = "Amuzu" 
#print(type(name))
#print(type(name) == str)
#print(isinstance(name, str))

#constractior function
#pizza = str("pepperoni")
#print(type(pizza))
#print(type(pizza) == str)
#print(isinstance(pizza, str))

# Concatination
fullname = name + " " + surname
print(fullname)

#casting a number to a stinge
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s." 
print(statement)

#multiple lines
multiline = """
Hey, how are you?

I was just checking up on you.
                        All good?
""" 
print(multiline)

#Escaping special characters
sentence = 'I\'m back to work!\tHey!\n\nwhere\'s this at \\located?'
print(sentence)


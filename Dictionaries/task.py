programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

print(programming_dictionary["Function"])

programming_dictionary["loop"] = "The action od doing something over and over again"

print(programming_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

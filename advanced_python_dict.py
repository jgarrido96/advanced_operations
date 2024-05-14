import time
# Task 1: Implement a function to merge two dictionaries, preserving the values of common keys from the second dictionary. Analyze the time and space complexity of this operation.

muscle_cars = {
    "Ford": "Mustang",
    "Chevrolet": "Camaro",
    "Dodge": "Challenger"
}

suv = {
    "Mercury": "Marauder",
    "Dodge": "Durango",
    "Subaru": "Ascent"
}

def new_dict(d1, d2):
    d1.update(d2)
    return d1

start_time = time.time()

print(new_dict(muscle_cars, suv))

end_time = time.time()
insert_time = end_time - start_time
print("Time taken to update dictionaries:", insert_time)

print('\n')

muscle_cars = {
    "Ford": "Mustang",
    "Chevrolet": "Camaro",
    "Dodge": "Challenger"
}

suv = {
    "Mercury": "Marauder",
    "Dodge": "Durango",
    "Subaru": "Ascent"
}

def intersection(d1, d2):
    for i in d1:
        if i in d2:
            print([{i: d1[i]}, {i: d2[i]}])

start_time = time.time()

intersection(muscle_cars, suv)

end_time = time.time()
insert_time = end_time - start_time
print("Time taken to find identical keys:", insert_time)

print('\n')
fruits = ['apples', 'pear', 'grape', 'banana', 'orange', 'grape', 'kiwi', 'mango', 'strawberry', 'pear']



def unique(array):
    new_array = []
    dictionary = {}
    for fruit in array:
        if fruit not in new_array:
            dictionary.update({fruit: 1})
            new_array.append(fruit)
        else:
            dictionary[fruit] += 1
    return new_array, dictionary

start_time = time.time()

print(unique(fruits))

end_time = time.time()
insert_time = end_time - start_time
print("Time taken to find unique items:", insert_time)

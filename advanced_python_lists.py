import time

# Task 1: Implement a function to create a new list using list comprehension that contains squares of numbers from 1 to n, where n is a parameter. Analyze the time and space complexity of this operation.
def squared(n):
    new_list = [x**2 for x in range(1, n + 1)]
    return new_list

start_time = time.time()

print(squared(8))

end_time = time.time()
access_time = end_time - start_time
print("Time taken to square numbers: ", access_time)



# Task 2: Implement a function to reverse a sublist within a list from index i to j (inclusive). Analyze the time and space complexity of this operation

fruits = [['apples', 'banana'], ['orange', 'grape'], ['kiwi', 'mango'], ['strawberry', 'pear']]

def reversed_sublist(list, i, j):
    for index in range(i, j):
        last_item = list.pop(j)
        list.insert(index, last_item)
    return list

start_time = time.time()

print(reversed_sublist(fruits, 1, 2))

end_time = time.time()
access_time = end_time - start_time
print("Time taken to reverse items: ", access_time)

# Task 3: Implement a function to merge two sorted lists into a single sorted list. Analyze the time and space complexity of this operation.

words1 = ['apples', 'banana', 'grape', 'orange']
words2 = ['kiwi', 'mango', 'pear', 'strawberry']

nums1 = [1, 3, 5, 7, 9]
nums2 = [2, 4, 6, 8, 10]

def new_sorted(num1, num2):
    for num in num2:
        num1.append(num)
    num1.sort()
    return num1

start_time = time.time()


print(new_sorted(nums1, nums2))

end_time = time.time()
access_time = end_time - start_time
print("Time taken to sort joined list of numbers: ", access_time)

start_time = time.time()

print(new_sorted(words1, words2))

end_time = time.time()
access_time = end_time - start_time
print("Time taken to sort joined list of words: ", access_time)

# LEVEL 1
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print(len(it_companies)) #1
it_companies.add('Twitter') #2
print(it_companies)

it_companies.update(['Lenovo','Samsung','Dell'])
print(it_companies) #3

random_pop = it_companies.pop() #4
print(f"We have randomly selected {random_pop} and removed it from the set.")

# diff_test = input('Enter a random value to test: ')
#! random_pop2 = it_companies.remove(diff_test)

'''
The difference between .discard() and .remove() is that .remove() raises a key error if item to be
deleted was not found while .discard() doesn't. #* #5
'''

# LEVEL 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# AB = A + B
# print(AB)
# I forgot how sets work lol

A_union_B = A.union(B) #1
print(A_union_B)

A_intersection_B = A.intersection(B) #2
print(A_intersection_B)

print(f'"A is a subset of B."\nThe above sentence is a {str(A.issubset(B)).lower()} statement.') #3

print(f'"A and B are disjoint sets."\nThe above sentence is a {str(A.isdisjoint(B)).lower()} statement.') #4

AB = A.union(B) #5
print(AB)
BA = B.union(A)
print(BA)

print(f"The symmetric difference between A and B is {A.symmetric_difference(B)}") #6
print(f"The difference between B and A is {B.difference(A)}")

del A #7
del B

# LEVEL 3
age = [22, 19, 24, 25, 26, 24, 25, 24]

ageset = set(age)
print(age, ageset)
print(f"The difference between length of age list and length of age set is {abs(len(age) - len(ageset))}") #2 (List is bigger)

# string VS list VS tuple VS set #2

#*   (Data Type)     (Definition)            (Indexed?)       (Modifiable?)
#     string        bunch of characters      YES                YES
#     list          bunch of items           YES                YES
#     tuple         bunch of items           YES                NO
#     set           bunch of items           NO                 NO

sentence = "I am a teacher and I love to inspire and teach people."
sentence_list = sentence.split()
print(sentence_list)
sentence_set = set(sentence_list)
print("The unique words used in the sentence are:\n", sentence_set)
#dictionaries are useful bc they allow us top group together and tag related pieces of information


# left hand side is key and right hand side is the actual value (the defijituoion of the word)

# key value : {Key: Value} => {Bug: An error in the program that prevents the program from u=running as expected}
#if you wanna have more than one value pair in your dictionary, you separate them using a comma 
#programming_dictionary ={
#   "Bug" : "An error in the program that prevents the program from running as expected.", 
#   "Function": "A piece of code that you can easily call over and over again." }

'''programming_dictionary = {
    "Bug" : "An error in the program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}
print(programming_dictionary["Bug"])

programming_dictionary["Loop"] = "The action of doing something over and over again in a program."

print(programming_dictionary)'''


# empty_dictionary = {}

# empty_dictionary["first_key"] = "This is my first key"
# empty_dictionary["second_key"] = "This is my second key"
# print(empty_dictionary)


# for key in empty_dictionary:
#     print(key)
#     print(empty_dictionary[key])
# In order to wipe and entire dictionary, 

# loop thru a dictionary


# student_scores = {
#     "Alice": 95,
#     "Bob": 82,
#     "Charlie": 68,
#     "Diana": 74
# }

# student_grades = {}

# # for student, score in student_scores.items():
# #     # logic for assigning grades goes here

# for student, score in student_scores.items():
#     if score >= 90:
#         grade = "A"
#     elif score >= 80:
#         grade = "B"
#     elif score >= 70:
#         grade = "C"
#     else:
#         grade = "Fail"
#     student_grades[student] = grade
# for student, score in student_scores.items():
#     if score >= 90:
#         grade = "A"
#     elif score >= 80:
#         grade = "B"
#     elif score >= 70:
#         grade = "C"
#     else:
#         grade = "Fail"
#     student_grades[student] = grade
# print(student_grades)
# Output: {'Alice': 'A', 'Bob': 'B', 'Charlie': 'Fail', 'Diana': 'C'}



'''NESTED DICTIONARIES'''

travel_log = {
  "France" :{
      "cities_visited" : ["Paris", "Lille", "Dijon"],
      "total_visits" : "12"
  },
  "Germany": {
      "cities_visited": ["Stuttgart", "Berlin", "Hamburg"],
      "total_visits" : "5"
    }
}
print(travel_log["France"]["cities_visited"][0])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])
# myfamily = {
#     "Child1" : {
#         "name" : "Mike",
#         "year" : 2004
#     },
#     "Child2" : {
#         "name" : "Alex",
#         "year" : 2005
#     },
#     "Child3" : {
#         "name": "Kate",
#         "year": 2006
#     }
# }
# for x, obj in myfamily.items():
#     print(x)
    # for y in obj: 
    #     print(y + ':', obj[y])


# a = {'name' : 'John', 'age' : 20}
# b = {'name' : 'May', 'age' : 23}
# customers = {'c1' : a, 'c2' : b}
# for x, obj in customers.items():
#   print(x)
    
#   for y in obj:
#     print(y + ':', obj[y]

# a = {'name' : 'John', 'age' : 85}
# b = {'name' : 'Jack', 'age' : 90}
# geriatrics = {'g1' : a, 'g2' : b}

# for x, obj in geriatrics.items():
#   print(x)
#   for y in obj:
#     print(y + ':', obj[y])
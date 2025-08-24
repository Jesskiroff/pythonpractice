test_scores = [88, 92, 76, 85, 90,
67, 73, 81, 95, 78,
84, 91, 69, 100, 58,
87, 93, 72, 66, 80,
77, 89, 94, 62, 71,
]

# sum = 0
# for score in test_scores:
#     sum += score
# print(sum)
# number_of_scores = len(test_scores)
# print(sum/number_of_scores)

max_score = 0
for score in test_scores:
    if score > max_score:
        max_score = score
print (max_score)
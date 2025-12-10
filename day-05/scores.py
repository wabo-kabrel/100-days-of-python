# Getting the total and maximum scores in a list using in-built functions and for-loops.

scores = [20, 10, 19, 15]

print(sum(scores))
print(max(scores))

total_scores = 0
greatest_score = 0

for i in scores:
    total_scores = total_scores + i    
print(total_scores)

for x in scores:
    if x > greatest_score:
        greatest_score = x
print(greatest_score)
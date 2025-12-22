name_1 = input("Enter your name: ").lower()
name_2 = input("Enter your lover's name: ").lower()

love_count = 0
true_count = 0

for i in name_1:
    if i in "love":
        love_count += 1

    if i in "true":
        true_count += 1

for i in name_2:
    if i in "love":
        love_count += 1

    if i in "true":
        true_count += 1

love_score = love_count + true_count

print(f"Your love score is {love_score}")

# Problem: Find max, min, sum, average of a list

user_list = []

for i in range(5):
    num = int(input("Enter a number: "))
    user_list.append(num)

# Max
max_val = user_list[0]
for num in user_list:
    if num > max_val:
        max_val = num

# Min
min_val = user_list[0]
for num in user_list:
    if num < min_val:
        min_val = num

# Sum
total = 0
for num in user_list:
    total += num

avg = total / len(user_list)

print("Max:", max_val)
print("Min:", min_val)
print("Sum:", total)
print("Avg:", avg)

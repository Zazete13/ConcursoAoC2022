calories_list = open("inputdia1.txt", "r").read().splitlines()
total_calories_list = []
total = 0

for i in calories_list:
    if i == "":
        total_calories_list.append(total)
        total = 0
    else:
        total += int(i)

total_calories_list.sort(reverse=True)
print(total_calories_list[0])
print(total_calories_list[0] + total_calories_list[1] + total_calories_list[2])

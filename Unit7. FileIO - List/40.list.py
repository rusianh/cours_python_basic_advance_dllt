colors = ["red", "green", "blue"]

print(colors)
print(colors[0])
print(colors[1])
print(colors[2])

print(len(colors))

colors.append("yellow")

print(colors)
print(colors[3])

for i in range(4): #hard code: nên đổi 4 = len(colors) vì biết đây là 4
    print(colors[i])

last_index = len(colors) - 1
print(colors[-1]) # -1 là vị trí thằng cuối cùng
print(colors[last_index])
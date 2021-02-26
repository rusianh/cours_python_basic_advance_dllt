# file = open("data.txt", "w")
with open("data.txt", "w") as file:
    file.write("dunglai\n")
    file.write("dunglailaptrinh")
# file.close() #khi mở một file mới thì phải có close (không)

with open("data.txt", "w") as file:
    file.write("a\n")
    file.write("b\n")
# file.close()

with open("data.txt", "a") as file:
    file.write("c\n")
    file.write("d\n")
# file.close()

with open("data.txt", "r") as file:
    data = file.read()
    print(data)
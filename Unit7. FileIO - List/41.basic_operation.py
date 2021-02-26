colors = ["red", "green", "blue", "yellows, red"]
print(colors)

# colors.remove("greenl") #validation: kiem tra nhung truong hop code khong hoat dong

#remove from list
try:
    colors.remove("green")
except:
    print("not exist") #chạy thử trong try trước nếu có lỗi thì chạy except

print(colors)

colors.pop() #remove last element
print(colors)

colors.insert(0, "black")
colors.insert(1, "purple")
print(colors)

print(colors.index("red"))

#find index of "red" in list
red_index = []
for i in range(len(colors)):
    if colors[i] == "red":
        red_index.append(i)

print(red_index)

# find number of occurance of "red"
print(colors.count("red"))

a = [1,2,10,4,5,0,6]
a.sort()
print(a)

a[0] = "dunglai" # thay đôi tương đương

#khi gặp một list bặn có thể truy cập, tìm vị trí, sửa dược nó, thêm bớt sửa xóa, và lặp từ đầu đến cuối : 
# kiểm soát được nó 
#String cũng như vậy: bản chất cũng là list ex: "dung" , string[2] là n
file = open("data.txt", "r") #"w": mode writing tạo file mới xóa file cũ, 
                            #"r" reading, "a" writing appending - ghi file mới, ghi thêm nhưng không xóa đi

# file.write("dunglai")
data = file.read() # đằng sau dấu chấm sẽ là một hành động gì đấy, một thuộc tính gì đấy. Đằng trước là một vật thể
print(data)


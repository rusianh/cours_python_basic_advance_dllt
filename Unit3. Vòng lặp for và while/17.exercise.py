# X = 0
# for i in range(3,100,2):
#     X = X + (1/i)

# print(X)


#cach 2
# X = 0 
# for i in range(1,100,2):
#     if i == 1:
#         continue
#     X = X + (1/i)

# print(X)

#cach 3
X = 0
for i in range(100):
    if i % 2 == 0 or i == 1:
        continue
    X = X + (1/i)

print(1/X)
print(round(1/X,2))

#module phần dư, division/devided chia, 

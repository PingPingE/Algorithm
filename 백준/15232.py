R = int(input())
C = int(input())
str =""
for i in range(R):
    for j in range(C):
        str += "*"
    if i != R-1:
        str += "\n"

print(str)
    

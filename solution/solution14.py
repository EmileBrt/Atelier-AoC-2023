with open('input/input_14.txt') as f:
    data = f.readlines()

for i,_ in enumerate(data):
    data[i] = data[i].replace("\n","")
    data[i] = list(data[i])

def IsSlided():
    for i in range(1,len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "O" and data[i-1][j] == ".":
                return False
    return True

while IsSlided() == False:
    for i in range(1,len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "O" and data[i-1][j] == ".":
                data[i][j], data[i-1][j] =  data[i-1][j],data[i][j]

print("Done")
#for d in data:
#    S = ''.join(d)
#    print(S)

S = 0

for i in range(len(data)):
    S += ''.join(data[i]).count("O") * (len(data) - i)

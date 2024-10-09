from copy import deepcopy

with open('input/input_14.txt') as f:
    data = f.readlines()

for i,_ in enumerate(data):
    data[i] = data[i].replace("\n","")
    data[i] = list(data[i])

def rotate_matrix_90_clockwise(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

def IsSlided(d):
    for i in range(1,len(d)):
        for j in range(len(d[i])):
            if d[i][j] == "O" and d[i-1][j] == ".":
                return False
    return True

def Slide(d_in):
    d = deepcopy(d_in)
    while IsSlided(d) == False:
        for i in range(1,len(d)):
            for j in range(len(d[i])):
                if d[i][j] == "O" and d[i-1][j] == ".":
                    d[i][j], d[i-1][j] =  d[i-1][j],d[i][j]
    return d

def Cycle(d_in): # North West South East
    d = deepcopy(d_in)
    for _ in range(4):
        d = Slide(d)
        d = rotate_matrix_90_clockwise(d)
    return d

cached = {}
for i in range(1_000_000_000):
    if str(data) in cached:
        break
    cached[i] = data
    cached[str(data)] = i
    data = Cycle(data)
offset = cached[str(data)]

data = cached[(1_000_000_000 - offset) % (len(cached) / 2 - offset) + offset]
S = 0
for i in range(len(data)):
    S += ''.join(data[i]).count("O") * (len(data) - i)
print(f"{S= }")
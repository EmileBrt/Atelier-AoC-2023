import json

with open('input/input_10.txt') as f:
    data = f.readlines()

for i,_ in enumerate(data):
    data[i] = data[i].replace("\n","")

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "S":
            print(f"START {i} {j} ")
            start = [i,j]

pipe = {
    "|" : {str([1,0]):[1,0],str([-1,0]):[-1,0]},
    "-" : {str([0,1]):[0,1],str([0,-1]):[0,-1]},
    "L" : {str([1,0]):[0,1],str([0,-1]):[-1,0]},
    "J" : {str([0,1]):[-1,0],str([1,0]):[0,-1]},
    "7" : {str([0,1]):[1,0],str([-1,0]):[0,-1]},
    "F" : {str([0,-1]):[1,0],str([-1,0]):[0,1]}
}
def next():
    return [loop[-1][0] + dir[0] , loop[-1][1] + dir[1]]

loop = [start]
dir = [0,-1] # up

print(f"{loop=}")
print(f"{next()=}")

while next() not in loop:

    n = next()

    n_char = data[n[0]][n[1]]

    #print(f"{n_char=} {n=}")

    loop.append(n)

    dir = pipe[n_char][str(dir)]

print(f"RES : {len(loop)//2}")


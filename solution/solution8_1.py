import math as mt
with open('input8.txt') as f:
    data = f.readlines()

for i,_ in enumerate(data):
    data[i] = data[i].replace("\n","")

path = data[0]

map = data[2:]
d_map = {}
for i,_ in enumerate(map):
    key = map[i].split(" = ")[0]
    left = map[i].split("(")[1].split(",")[0]
    right = map[i].split(", ")[1].split(")")[0]
    d_map[key] = {"L":left,"R":right}

states = []

# def end(states):
#     isZ = []
#     for s in states:
#         if s[-1] == 'Z':
#             isZ.append(1)
#     if sum(isZ) == len(states):
#         return True
#     else:
#         return False
    
for key in d_map.keys():
    if key[-1] == "A":
        if key not in states:
            states.append(key)

print(f"{states}")
steps = []
for i,state in enumerate(states):
    c = 0
    while states[i][-1] != "Z":
        states[i] = d_map[states[i]][path[c%len(path)]]
        c += 1
    steps.append(c)
print(f"{steps=}")
R = mt.lcm(steps[0],mt.lcm(steps[1],mt.lcm(steps[2],mt.lcm(steps[3],mt.lcm(steps[4],steps[5])))))
print(f"{R=}")
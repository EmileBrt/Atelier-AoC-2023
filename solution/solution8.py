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

state = "AAA"
c = 0
while state != "ZZZ":
    state = d_map[state][path[c%len(path)]]
    c += 1
print(f"{c=}")
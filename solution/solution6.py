Time = [38, 94, 79, 70]
Distance = [241, 1549, 1074, 1091]

r = []
for j, t in enumerate(Time):
    ri = 0
    for i in range(t):
        if (i * (t - i)) > Distance[j]:
            ri += 1
    r.append(ri)

S = 1
for ri in r:
    S *= ri
print(f"{S=}")

Time = [38947970]
Distance = [241154910741091]

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

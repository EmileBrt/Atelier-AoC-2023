with open("input/input_1.txt") as f:
    data = f.readlines()
digits = list(range(10))
for i in range(len(digits)):
    digits[i] = str(digits[i])

s = 0
for l in data:
    r = ""
    for k in l:
        if k in digits:
            r += k
    if r != "":
        s += int(r[0] + r[-1])

print(f"{s=}")

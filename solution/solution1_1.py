with open("input/input_1_2.txt") as f:
    data = f.readlines()


digits = list(range(1, 10))
for i in range(len(digits)):
    digits[i] = str(digits[i])

digits_str = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

print(f"{digits=}")
print(f"{digits_str=}")

s = 0
for i in range(len(data)):
    r = ""
    for j in range(len(data[i])):
        if data[i][j] in digits:
            r += data[i][j]
        else:
            for k, dig in enumerate(digits_str):
                if j + len(dig) - 1 <= len(data[i]):
                    if data[i][j : j + len(dig)] == dig:
                        r += str(k + 1)
    s += int(r[0] + r[-1])

print(f"{s=}")

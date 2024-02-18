int = 10

sequence = [int]
while int != 1:
    if int % 2 == 0:
        int = int // 2
    else:
        int = 3 * int + 1
    sequence.append(int)
print(sequence)



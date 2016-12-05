num = int(input("Enter a starting number: "))
size = int(input("Enter the sequence size: "))
seq = []
for i in range (0, size):
    if i == 0 or i == 1:
        seq.append(num)
    else:
        seq.append(seq[i-1] + seq[i-2])
    print(seq[i]," ")

with open(".rosalind/cons-1778970318031.txt", "r") as f:
    lines = f.read().splitlines()

dna = []
part_seq = ""
for i in lines:
    if i[0] != ">":
        part_seq += i
    else:
        if part_seq:
            dna.append(part_seq)
        part_seq = ""

if part_seq:
    dna.append(part_seq)

a = []

for i in range(len(dna[0])):
    curr = [0, 0, 0, 0]
    for string in dna:
        c = string[i]

        if c == 'A':
            curr[0] += 1
        elif c == 'C':
            curr[1] += 1
        elif c == 'G':
            curr[2] += 1
        else:
            curr[3] += 1
        
    a.append(curr)

ans = ""
aList = []
cList = []
gList = []
tList = []
for i in a:
    index = 0
    currMax = 0
    for j in range(len(i)):
        if i[j] > currMax:
            index = j
            currMax = i[j]
            
    if index == 0:
        ans += "A"
    elif index == 1:
        ans += "C"
    elif index == 2:
        ans += "G"
    else:
        ans += "T"
    aList.append(i[0])
    cList.append(i[1])
    gList.append(i[2])
    tList.append(i[3])

    
with open(".rosalind/ans.txt", "w") as f:
    f.write(ans)
    f.write("\n")
    f.write("A: " + " ".join(str(x) for x in aList))
    f.write("\n")
    f.write("C: " + " ".join(str(x) for x in cList))
    f.write("\n")
    f.write("G: " + " ".join(str(x) for x in gList))
    f.write("\n")
    f.write("T: " + " ".join(str(x) for x in tList))

# holy unoptimized code. 
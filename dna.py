with open(".rosalind/dna-1778295869076.txt") as f:
    dna = f.read().strip()

ans = [0] * 4

for base in dna:
    if base == "A":
        ans[0] += 1
    elif base == "C":
        ans[1] += 1
    elif base == "G":
        ans[2] += 1
    elif base == "T":
        ans[3] += 1

print(ans[0], ans[1], ans[2], ans[3])
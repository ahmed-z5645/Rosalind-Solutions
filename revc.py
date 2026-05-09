with open(".rosalind/revc-1778298272490.txt") as f:
    dna = f.read().strip()

ans = ""

for base in dna:
    if base == "A":
        ans += "T"
    elif base == "T":
        ans += "A"
    elif base == "G":
        ans += "C"
    elif base == "C":
        ans += "G"

ans = ans[::-1]

print(ans)

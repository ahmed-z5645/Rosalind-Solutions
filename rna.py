with open(".rosalind/rna-1778297483783.txt") as f:
    rna = f.read().strip()

ans = ""

for base in rna:
    if base == "A":
        ans += "A"
    elif base == "T":
        ans += "U"
    elif base == "G":
        ans += "G"
    elif base == "C":
        ans += "C"

print(ans)
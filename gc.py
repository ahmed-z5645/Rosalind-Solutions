with open('.rosalind/gc-1778368155951.txt') as f:
    dna = f.read().strip()

dna_list = dna.split('>')[1:]

maxGC = 0

for seg in dna_list:
    parts = seg.split('\n')

    title = parts[0]

    gcCount = 0
    length = 0
    for i in range(1, len(parts)):
        for base in parts[i]:
            if base == 'G' or base == 'C':
                gcCount += 1
            length += 1

    if (gcCount / length) > maxGC:
        maxGC = (gcCount / length)
        maxTitle = title
    
print(maxTitle)
print(round(maxGC * 100, 6))
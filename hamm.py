with open('.rosalind/hamm-1778368955915.txt') as f:
    strands = f.read().split('\n')

s, t = strands[0], strands[1]

if len(s) != len(t):
    print("what")
else:
    mutations = 0

    for i in range(len(s)):
        if s[i] != t[i]:
            mutations += 1
    
    print(mutations)
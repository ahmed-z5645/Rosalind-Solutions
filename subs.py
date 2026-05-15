with open('.rosalind/subs-1778817967862.txt', 'r') as f:
    s = f.readline().strip()
    t = f.readline().strip()

ans = []

left = 0


while left < len(s):
    if s[left] == t[0]:
        right = left
        while (right < left + len(t) - 1) and (right < len(s) - 1):
            right += 1
            if s[right] != t[right - left]:
                break
            elif (right - left) == (len(t) - 1):
                ans.append(left + 1)
    left += 1

print(ans)
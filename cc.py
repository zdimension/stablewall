# expected: -1
inp = [
    "XXOO",
    "XFFO",
    "XFXO",
    "XXXO"
]

# expected: EDCBA
inp = [
    "AAABBCCDDE",
    "AABBCCDDEE",
    "AABBCCDDEE"
]

# expected: ABCDE
inp = [
    "ABBCCDDEEE",
    "AABBCCDDEE",
    "AABBCCDDEE"
]

# expected: ZOMA or ZOAM
inp = [
    "ZOAAMM",
    "ZOAOMM",
    "ZOOOOM",
    "ZZZZOM"
]

wid = len(inp[0])

chars = {c: set() for line in inp for c in line}

for x in range(wid):
    for i in range(len(inp) - 1):
        chars[inp[i][x]].add(inp[i + 1][x])

ans = []

while chars:
    for c, l in chars.items():
        if (l - {c}).issubset(ans):
            ans.append(c)
            del chars[c]
            break
    else:
        ans = []
        break

print(ans or -1)

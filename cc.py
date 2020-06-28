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

# compute the adjacency matrix

# for each distinct character in the grid, create an empty set
chars = {c: set() for line in inp for c in line}

# fill that set with all the supporting letters
for x in range(wid):
    for i in range(len(inp) - 1):
        chars[inp[i][x]].add(inp[i + 1][x])

ans = []

# while there are letters to add
while chars:
    # find the first letter that can be added
    # i.e. find the first letter whose supporting letters are all present
    for c, l in chars.items():
        # l - {c} gives all the supporting letters excluding the letter itself, to prevent cycles
        if (l - {c}).issubset(ans):
            ans.append(c)
            del chars[c]
            break
    else:
        ans = []
        break

print(ans or -1)

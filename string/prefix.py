def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""
    
    strs.sort()
    first = strs[0]
    last = strs[-1]

    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return first[:i]
    
    return first

def alternate(strs: list[str]) -> str:
    if not strs:
        return ""
    
    strs.sort()
    first = strs[0]
    last = strs[-1]

    ans = []

    for i in range(min(len(first), len(last))):
        print(ans)
        if first[i] != last[i]:
            return ''.join(ans)
        ans.append(first[i])
    return ''.join(ans)

print(alternate(["flower","flow","flight"]))
print(alternate(["dog","racecar","car"]))
print(alternate(["ab","a"]))
print(alternate(["cir","car"]))
print(alternate(["a"]))

s = "flowerGarder"

print(", ".join(s))  # f, l, o, w, e, r, G, a, r, d, e, r
print("".join(s))  # flowerGarder
print("-".join(s))  # f-l-o-w-e-r-G-a-r-d-e-r
print(" ".join(s))  # f l o w e r G a r d e
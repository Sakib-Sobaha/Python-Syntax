def largestEven(s: str) -> str:
    for i in range(len(s)-1, -1, -1):
        if int(s[i]) % 2 == 0:
            return s[:i+1]
    return ""

s = "54321"
print(largestEven(s))  # Output: "5432"
print(s[1:4]) # Output: "432"
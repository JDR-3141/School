import itertools

def check(n):
    s = []
    for i in range(0, 10, 2):
        s.append(int(n[i] + n[i+1]))
    d = s[1]-s[0]
    for i in range(2, 5):
        if s[i]-s[i-1] != d:
            return 0
    return sum(s)

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
permutations = list(itertools.permutations(numbers))
value = 0
for n in permutations:
    value += check(n)

n = ["1", "8", "3", "6", "5", "4", "7", "2", "9", "0"]
s = []
for i in range(0, 10, 2):
    s.append(int(n[i] + n[i+1]))
print(s)
d = s[1]-s[0]
print("Common difference", d)
for i in range(2, 5):
    if s[i]-s[i-1] != d:
        print(0)
print(sum(s))


print(value)



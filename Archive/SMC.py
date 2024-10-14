i = 999999
while True:
    if i % 18 == 0:
        text = str(i)
        if text[:3] == text[5:2:-1]:
            break
    i -= 1
print(i)
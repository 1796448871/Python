size=int(input())
for _ in range(size):
    s=input()
    count = 0
    for char in s:
        if char.isdigit():
            count += 1
    print(count)
n = int(input())
ar = input().split(" ")
if len(ar) != n:
    print(f"enter only {n} socks color")
else:
    pair = set()

    pair = []
    p_color = []
    for i in ar:
        if i not in p_color: 
            pair.append(ar.count(i))
            p_color.append(i)
    result = 0
    for i in pair:
        result += int(i)//2
    print(result)

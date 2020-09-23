

while True:
    try:
        n = int(input())
        group_s = []
        for i in range(n):
            s = input()
            if not s:continue
            if len(s) <= 8:
                group_s.append(s + "0"*(8 - len(s)))
            if len(s) > 8:
                if len(s) % 8 != 0:
                    group_s += [s[i*8:min(i*8+8, len(s))] for i in range(len(s)//8+1)]
                else:
                    group_s += [s[i*8:min(i*8+8, len(s))] for i in range(len(s)//8)]
        for i in group_s:
            print(i + "0"*(8 - len(i)))
    except: break
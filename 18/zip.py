def zip(seznam1, seznam2):
    z = 0
    seznam4 = []
    x = len(seznam1)
    o = len(seznam2)
    if x > o:
        p = x - o
        x = x - p
    t = 0
    u = 0
    while z != x:
        seznam3 = (seznam1[t], seznam2[u])
        seznam4.append(seznam3)
        z = z + 1
        t = t + 1
        u = u + 1
    print(seznam4)

    t = 0
    u = 0
    z = 0
    if x > o:
        p = x - o
        x = x - p
    while z != x:
        seznam3 = seznam1[t] + "\n" +seznam2[u]
        print(seznam3)
        z = z + 1
        t = t + 1
        u = u + 1

zip(["1", "2", "3", "4", "5"], ["a", "b", "c", "d", "f", "e"])

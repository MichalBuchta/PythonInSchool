sl = ""

def vypis_cisel(sl, n):
    """
    Zadejte s pro sude nebo l pro liche je to case sensitive. Jako druhy argument zadejte kolik cisel to ma vypsat.
    program vypise prvni N s/l cisel pomoci while loopu.
    """
    if sl == "s":
        x,y = 0,0

        while x != n:
            x = x + 1
            y = y + 2
            print(y)
    elif sl == "l":
        x,y = 0,-1

        while x != n:
            x = x + 1
            y = y + 2
            print(y)
vypis_cisel("s", 6)

def vypis_cisel2(sl, n):
    if sl == "s":
        for x in range(1,n*2+1):
            if x % 2 == 0:
                print(x)
    elif sl == "l":
        for x in range(1,n*2):
            if x % 2 == 1:
                print(x)
vypis_cisel2("l", 6) 
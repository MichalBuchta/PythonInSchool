birthday = input("zadej rodny cislo: ")

year = birthday[0:2]
month = birthday[2:4]
day = birthday[4:6]


if int(year) >= 23:
    print("Narodil jsem se ",day,".",month,".19",year,sep="")
    y = 1900 + int(year)
    rok = 2022-y+1
    print("V letošním roce dosáhnu", rok)
else:
    print("Narodil jsem se ",day,".",month,".20",year,sep="")
    y = 2000 + int(year)
    rok = 2022-y+1
    print("V letošním roce dosáhnu", rok)
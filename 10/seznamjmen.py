seznam = ['Adam', 'Eduardo', 'Filip', 'Eda', 'Adam2']

for loop in seznam:
    if len(loop) > 4:
        z = loop.upper()
        print(z, len(z))
    else:
        s = loop.lower()
        print(s, len(s))
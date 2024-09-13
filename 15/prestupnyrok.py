def prestupny_rok(x):
    """Funkce je rok funkci jedne promenne, nezaporneho celeho cisla
    Program po zadani vypise zda je rok prestupny ci nikoliv."""
    if x % 4 == 0 and (x % 100 != 0 or x % 400 == 0):
        print("rok",x,"je prestupny")
    else:
        print("rok",x," neni prestupny")

prestupny_rok(2000)
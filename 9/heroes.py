heroes = ["Hulk", "Mr Incredible", "Elastigirl", "Dash", "Frozone", "Captain America", "Flash", "Batman", "Arrow",
          "Baymax", "Superman", "Black Widow", "Hawkeye", "Quicksilver", "Magneto", "Wolverine", "Harley Quinn",
          "Poison Ivy", "Wasabi", "Mr Invisible", "Hiro", "Iron Man", "Joker", "Wonder Woman", "Deadpool", "Hellboy",
          "Captain Boomerang", "Green Lantern", "She-Ra", "Spiderman", "Storm"]

heroes.append("Aquaman")
if "Aquaman" in heroes: print("Aquaman je tu")
if "Aquaman" not in heroes: print("Aquaman tu neni")
if "Mr Invisible" in heroes: print("Mr Invisible je na vecirku")
if "Iron Man" in heroes: print("Iron Man se nam dostal na vecirek")
x = len(heroes)
print("Na vecirku je: ",x)
print("tombolu vyhrali",heroes[3-1], heroes[14-1], heroes[27-1])

padousi = []
padousi.append("Loki")
padousi.append("Huska")
padousi.append("Krocan")

if "Thor" in heroes: print("Lokimu se nepodarilo znicit vecirek")
if "Thor" not in heroes: print("Lokimu se podarilo znicit vecirek")
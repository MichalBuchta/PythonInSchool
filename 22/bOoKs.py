books = [
    {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
    {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
    {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019}
]

total_profit = 0
total_sold = 0

for book in books:
    if book["year"] == 2019:
        profit = book["price"] * book["sold"]
        total_profit += profit
        total_sold += book["sold"]
        print(book["title"], "bylo prodáno", book["sold"], "ks a zisk z něj byl", profit)

print("Knih bylo celkem prodáno: ", total_sold)
print("Celkovy zisk je: ", total_profit)
































"""l = len(books)
print(l)
 

x1 = books[0]
x2 = books[1]
x3 = books[2]

x1sold = x1["sold"]
x2sold = x2["sold"]
x3sold = x3["sold"]

xsold = x1sold + x2sold + x3sold

x1price = x1["price"]
x2price = x2["price"]
x3price = x3["price"]

xprice = x1price + x2price + x3price

zisk = xprice * xsold

x1year = x1["year"]
x2year = x2["year"]
x3year = x3["year"]

list = [x1year, x2year, x3year]

for rok in list:
    if rok == 2019:
        print(rok)

print("Knih bylo celkem prodáno: ", xsold)
print("Celkovy zisk je: ", zisk)"""




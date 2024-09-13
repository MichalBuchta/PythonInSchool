import statistics
cisla = [1.2, 8.6, 3.2]

def arit_pr(seznam):
    x = statistics.mean(seznam)
    print(round(x, 1))

arit_pr(cisla)

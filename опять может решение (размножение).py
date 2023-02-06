m = int(input("Cтартовое кол-во организмов"))
p = int(input("Cеднесуточное учеличение в %"))
n = int(input("Кол-во дней для размножения"))
for i in range(n):
    print(i + 1, m)
    m = m + p / 100 * m 

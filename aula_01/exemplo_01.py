a,b,c,d = map(int, input("mostre o valor: ").split())
sp = 0
si = 0
if a % 2 == 0: sp += a
else: si += a
if b % 2 == 0: sp += b
else: si += b
if c % 2 == 0: sp += c
else: si += c
if d % 2 == 0: sp += d
else: si += d
print ("soma dos pares:", sp)
print ("print dos impares", si)


l = [a, b, c, d]
lp = [x for x in l if x % 2 == 0]
li = [x for x in l if x % 2 == 1]
print ("soma dos pares", sum (lp))
print ("soma dos impares", sum (li))
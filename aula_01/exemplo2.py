a,b,c,d = map (int(input().split()))

l = [a, b, c, d]
l.sort()
if l [0] == l[1] or l[1] == l[2] or l[2] == l[3]:
    print ("existe algum valor repeito")
else: 
    menor = l [0]
    maior = l [3]
    soma = l[1] + l[2]
s1 = str(input())
s2 = str(input())

l1 = s1.split(" ")
l2 = s2.split(" ")

result = int(l1[1]) * float(l1[2]) + int(l2[1]) * float(l2[2])

print("VALOR A PAGAR: R$",'{:.2f}'.format(result) )

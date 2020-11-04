# A. 2+4*6-4
from operation import*
a = 2
b = 4
c = 6
print(a, "+", b, "*", c, "-", b, "=",kurang(jumlah(kali(b,c),a),b))

# B. (4+7) * (6-9)
from operation import*
a = 4
b = 7
c = 6
d = 9
print("(",a,"+",b,") x (",c,"-",d,")=",kali(jumlah(a,b),kurang(c,d)))

# C. (10+2) / (7+5) / (12-34)
a = 10
b = 2
c = 7
d = 5
e = 12
f = 34
print("(",a,"+",b,") / (",c,"+",d,") / (",e,"-",f,") =",bagi(bagi(jumlah(a,b),jumlah(c,d)),kurang(e,f)))

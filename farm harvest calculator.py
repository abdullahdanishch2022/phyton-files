farm1=120
farm2=85
farm3=150
farm4=95
farm5=110
total=farm1+farm2+farm3+farm4+farm5
avg=total/5
print("total harvest in kg",total)
print("average per feild in kg",avg)

priceperkg=15
earnings=total*priceperkg
print("total earnings are",earnings)

bags=total//25
leftover=total%25
print("full bags packed",bags)
print("leftover",leftover)

total+=30
print("after bonus crop",total)
total-=15
print("after seat reserved",total)
bags=total//25
print("final bags packed",bags)
earnings=total*priceperkg
print("total earnings are",earnings)
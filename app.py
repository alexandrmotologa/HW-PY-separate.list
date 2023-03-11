WINTER = (0,1,11)
SPRING = (2,3,4)
SUMMER = (5,6,7)
FALL   = (8,9,10)

profitYearly = [
        -500, 1000, # winter
  1100, 1100, 1000, # spring
   900, -800, -900, # summer
  1200, 1300, 1400, # fall
  1100              # winter
]

profit_winter = []
profit_spring = []
profit_summer = []
profit_fall   = []

for i in range(len(profitYearly)):
    profit = profitYearly[i]
    if i in WINTER:
        profit_winter.append(profit)
    if i in SPRING:
        profit_spring.append(profit)
    if i in SUMMER:
        profit_summer.append(profit)
    if i in FALL:
        profit_fall.append(profit)

print(profit_winter)
print(profit_spring)
print(profit_summer)
print(profit_fall)

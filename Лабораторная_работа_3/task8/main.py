money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
increase+=1
month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
while (money_capital+salary>spend):
    money_capital+=salary
    money_capital-=spend
    spend*=increase
    month+=1
print(month)

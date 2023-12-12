#ОПИ
start = 10000
# - спроектировать БД
# - создать макет сайта
# - написать код
# - протестировать систему
# - спроектировать систему
# - внедрить систему и обучить пользователей
# - создать модель анализа данных
# - собрать требования к системе

# программист
# тестировщик
# дизайнер
# верстальщик
# проектировщик
# спец по анализу данных
# системный аналитик
# спец по внедрению б.с.

a = [['программист', 'спроектировать БД', 200, 1300], 
    ['тестировщик', 'протестировать систему', 200, 1300],
    ['дизайнер', 'создать макет сайта', 250, 1000],
    ['верстальщик', 'написать код', 200, 1200],
    ['проектировщик', 'спроектировать систему', 300, 1700],
    ['спец по анализу данных', 'создать модель анализа данных', 400, 2000],
    ['системный аналитик', 'внедрить систему и обучить пользователей', 400, 2000],
    ["спец по внедрению бсист", 'собрать требования к системе', 500, 2200]]

c = []
quest = 'Нужно '
# for i in range(len(a)):
#     ans = input(f"{quest}{a[i][1]}")
b = 1
while b!= -1:
    print("\n")

    print("Введите номер нужной работы.")
    print("0 - спроектировать БД")
    print("1 - протестировать систему")
    print("2 - создать макет сайта")
    print("3 - написать код")
    print("4 - спроектировать систему")
    print("5 - создать модель анализа данных")
    print("6 - внедрить систему и обучить пользователей")
    print("7 - собрать требования к системе")

    print("Введите -1 если выбраны нужные работы.")
    
    num = int(input())
    if num != -1:
        c.append(num)
    else:
        b = num

print("\n")

print("Требуется(ются):")
countpersons = len(c)
for i in range (len(c)):
    print(f'{i+1}. {a[i][0]}')
print("\n")
rent = countpersons*2 + 10
outsourcing_rent = (countpersons*10 + countpersons*10 + rent*5 + countpersons*10 + rent*100 + countpersons*10)
print(f'Аутсорсинг и аренда = {outsourcing_rent}')


workingtime = len(c) * 1600

havetime = 0
salary = 0
for i in range(len(c)):
    havetime += a[i][3]
    salary += a[i][2]
salary = salary + countpersons*150
print(f'Зарплата = {salary }')
months = 0

d = [1600, 1600, 1600, 1600, 1600]
if havetime%1600!=0:
    months = havetime//1600 +1
else:
    months = havetime / 1600
if workingtime > 8000:
    for i in range(len(c)):
        while havetime < 8000:
            havetime += a[i][3]
            months +=1
print(f'Кол-во месяцев для выполнения работы = {months}')      
print(f'Требуемый капитал на старте = {outsourcing_rent*2+salary}')
print(f'Затраты на каждый месяц = {outsourcing_rent+salary}')

dohod_zakaz = 0
if (outsourcing_rent+salary)%1000==0:
    dohod_zakaz = outsourcing_rent+salary +1000
else:
    dohod_zakaz = (((outsourcing_rent+salary)//1000)+1)*1000

print(f'Доход от заказчика = {dohod_zakaz}')

if months>=5:
    print(f"Итоговая прибыль = {5*dohod_zakaz-months*(outsourcing_rent+salary)+(10000-(outsourcing_rent*2+salary))}")
else:
    print(f"Итоговая прибыль = {(1+(havetime//1600))*dohod_zakaz-months*(outsourcing_rent+salary)+(10000-(outsourcing_rent*2+salary))}")






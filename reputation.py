#Переменные
x = 1
rep = 50
FrSem = 100
FrShk = 30
FrDv = 15
FrGo = 0
FrProg = 0
Str = 50
Intel = 35
ChUm = 5
forma = 50
mendm = 5
name = input("Привет, Пользователь! Какое твое имя?(Если поле пустое - ,,Пользователь,,)")
if name == '':
    name == 'Пользователь'
#Исходник
#if ans == '1':
#    pass
#elif ans == '2':
#    pass
#elif ans == '3':
#    pass
#elif ans =='4':
#    pass
#Исходник
print("Интересы? (Ниже)")
while x!=2:
    print("Аниме - 1")
    print("csgo - 2")
    print("dota2 - 3")
    print("Сериалы - 4")
    print("фанфики - 5")
    ans = input("1-6, q - всё:   ")
    if ans == '1':
        pass
    elif ans == '2':
        pass
    elif ans == '3':
        pass
    elif ans =='4':
        pass
    else:
        x+=1
print(name, " какой ты класс? (Ниже варианты ответа)")
print("Бунтарь - 1")
print("Задира - 2")
print("Острослов - 3")
print("Тыжпрограммист - 4")
print("Тролль - 5")
ans = input("1-5:   ")
if ans == '1':
    FrSem-=50
    FrShk+=45
    FrDv+75
    FrGo+=1
    Str+=40
    Intel-=5
    ChUm-=5
    mendm+=5
    rep = (FrSem+FrShk+FrDv+FrGo)//4

elif ans == '2':
    Str+=45
    Intel-=20
    ChUm-=999
    FrSem-=101
    FrShk+=69
    FrDv+=5
    FrGo-=1
    rep = (FrSem+FrShk+FrDv+FrGo)//4
elif ans == '3':
    FrSem+=55
    FrShk-=10
    FrDv+=10
    FrGo+=0
    Intel+=65
    ChUm+=0
    forma-=30
    Str-=10
    mendm+=75
    rep = (FrSem+FrShk+FrDv+FrGo)//4

elif ans =='4':
    FrSem+=55
    FrShk-=10
    FrDv+=10
    FrGo+=0
    Intel+=65
    ChUm+=0
    forma-=30
    Str-=10
    mendm+=75
    rep = (FrSem+FrShk+FrDv+FrGo)//4
elif ans =='5':
    FrSem-=45
    FrShk-=99
    FrDv+=100
    FrGo+=1
    Intel+=0
    ChUm+=500
    forma-=100
    Str-=100
    mendm+=100
    rep = (FrSem+FrShk+FrDv+FrGo)//4
print(name, " твой результат: ")
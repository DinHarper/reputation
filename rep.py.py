y = 1
while y !=2:
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
    name = input("Привет, Пользователь! Какое твое имя?")

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
        print("Сериалы - 4") #а код читают? 
        print("фанфики - 5")
        print("Учеба - 6") #если да, то ты СУКА НАХУЙ ПИДАРЕСКА
        print("Кодинг - 7")
        print("Стихи - 8")
        print("Троллинг - 9")
        ans = input("1-9, q - всё:   ")
        if ans == '1':
            FrSem-=35
            FrShk-=35
            FrDv+=5
            FrGo+=1
            Str+=0
            Intel+=35
            ChUm+=25
            mendm+=65
        elif ans == '2':
            FrSem-=25
            FrShk+=25
            FrDv-=15
            FrGo+=1
            Str+=40
            Intel-=20
            ChUm-=5
            mendm+=55
        elif ans == '3':
            FrSem-=65
            FrShk-=45
            FrDv+=40
            FrGo+=1
            Str+=0
            Intel-=50
            ChUm-=25
            mendm+=45
        elif ans =='4':
            FrSem+=45
            FrShk-=45
            FrDv+=10
            FrGo+=1
            Str+=0
            Intel-=35
            ChUm-=15
            mendm+=55
        elif ans =='5':
            FrSem-=50
            FrShk+=0
            FrDv+=5
            FrGo+=100
            Str+=0
            Intel-=25
            ChUm-=35
            mendm+=45
        elif ans =='6':
            FrSem+=100
            FrShk-=100
            FrDv+=25
            FrGo+=1
            Str-=35
            Intel+=75
            ChUm-=5
            mendm+=85
        elif ans =='7':
            FrSem+=50
            FrShk-=25
            FrDv+=10
            FrGo+=1
            Str+=0
            Intel+=75
            ChUm+=5
            mendm+=85
        elif ans =='8':
           pass
        elif ans =='9':
            FrSem-=50
            FrShk+=45
            FrDv+=1
            FrGo+=1
            Str+=40
            Intel-=5
            ChUm-=5
            mendm+=5
        else:
            x+=1
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        
    print(name, " какой ты класс? (Ниже варианты ответа)")
    print("бунд - 1") 
    #нэвэльный иначе говоря
    print("гопнек - 2")
    print("мамкин философ - 3")
    print("Тыжпрограммист - 4")
    #посоны це я шарирую
    print("Тролль - 5")
    ans = input("1-5:   ")
    if ans == '1':
        FrSem-=50
        FrShk+=45
        FrDv+=75
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
    print(FrSem, " - у фракции семья")
    print(FrShk, " - у фракции дноклов")
    print(FrDv, " - у фракции гопников")
    print(Intel, " - интелект")
    print(Str, " - сила")
    print(ChUm, " - юмор")
    print(mendm, " - ментальный дмг")
    y = input("Еще раз? (Д/Н)")
    if y == "Д":
        pass
    else:
        y+=1

print("ля жопа")

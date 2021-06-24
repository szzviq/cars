def menu():
    print("Üdvözöljük a XY Autókereskedés oldalán! Kérjük válasszon az alábbi menüpontok közül:\n 1. Kocsi felvetel. \n 2. Osszes kocsi adatai lekerdezese \n 3. Kocsi adatainak lekerdezese index alapjan. \n 4. Kocsi eladasa\n 5. Kilépés")
#1.Itt be kell tudni adni az auto markajat es, hogy mennyi idos a kocsi. #

marka_list = []
kor_list = []
flag = True
while flag:
    try:
        usr_int = int(input("Válasszon menüpontot: "))

        if usr_int == 1:
            auto_marka = input("Kérjük adja meg az autó márkáját: ")
            auto_kor = int(input("Kérjük adja meg az auto korát: "))
            marka_list.append(auto_marka)
            kor_list.append(auto_kor)
        elif usr_int == 2:
            for marka, kor in zip(marka_list, kor_list):
                print(marka, kor)
        elif usr_int == 3:
            usr_index = int(input("Kérjük adja meg az autó indexét: "))
            print(marka_list[usr_index], kor_list[usr_index])
        elif usr_int == 4:
            marka_sell = input("Melyik autót kívánja eladni? ")
            kor_sell = int(marka_list.index(marka_sell))
            kor_list.remove(kor_list[kor_sell])
            marka_list.remove(marka_sell)
            # print(x)
            # for i in marka_list:
            #     marka_list.pop(x)
            # for i in kor_list:
            #     kor_list.pop(x)
        elif usr_int == 5:
            flag = False
        else:
            print("Kérjük válaszon a menüpontok közül: \n 1. Kocsi felvetel. \n 2. Osszes kocsi adatai lekerdezese \n 3. Kocsi adatainak lekerdezese index alapjan. \n 4. Kocsi eladasa\n 5. Kilépés")
    except ValueError:
        print("Kérjük számot adj meg!")
menu()
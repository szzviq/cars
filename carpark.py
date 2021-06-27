print("Üdvözöljük a XY Autókereskedés oldalán! Kérjük válasszon az alábbi menüpontok közül:")


def menu():
    print(" 1. Kocsi felvetel. \n 2. Osszes kocsi adatai lekerdezese \n 3. Kocsi adatainak lekerdezese index alapjan.")
    print(" 4. Kocsi eladasa\n 5. Kilépés")


def kocsi_felvetel():
    auto_marka = input("Kérjük adja meg az autó márkáját: ")
    auto_kor = int(input("Kérjük adja meg az auto korát: "))
    marka_list.append(auto_marka)
    kor_list.append(auto_kor)
    print("________________")


def adat_leker():
    for marka, kor in zip(marka_list, kor_list):
        print(marka, kor)
    print("________________")


def index_leker():
    usr_index = int(input("Kérjük adja meg az autó indexét: "))
    print(marka_list[usr_index], kor_list[usr_index])
    print("________________")


def auto_elad(marka_sell):
    # kor_sell = int(marka_list.index(marka_sell))
    # print(kor_sell)
    index =[]
    count = 0

    for i in marka_list:
        if i == marka_sell:
            index.append(count)
            kor_elad = kor_list[count]
            print(f"Önnek az {count}. indexen van {marka_sell} márkájú {kor_elad} éves autója")
        count += 1

    sell_index = int(input("Kérjük adja meg az eladni kívánt autó indexét: "))
    if sell_index in index:
        del marka_list[sell_index]
        del kor_list[sell_index]
        print(f"Ön eladta a {sell_index}. indexű {marka_sell} márkájú autót!")

    else:
        print("Nem megfelelő index.")
    print("________________")
    # kor_list.remove(kor_list[kor_sell])
    # marka_list.remove(marka_sell)




# 1.Itt be kell tudni adni az auto markajat es, hogy mennyi idos a kocsi. #
def start():
    flag = True
    while flag:
        try:
            menu()
            usr_int = int(input("Válasszon menüpontot: "))

            if usr_int == 1:
                flag2 = True
                kocsi_felvetel()
                while flag2:
                    new = input("Szeretne még egy autót felvinni? I/N ").lower()
                    if new == "i":
                        kocsi_felvetel()
                    elif new == "n":
                        flag2 = False
                    else:
                        print("Kérjük írjon be igent vagy nemet")
                        continue

            elif usr_int == 2:
                adat_leker()
                pass
            elif usr_int == 3:
                index_leker()
                pass
            elif usr_int == 4:
                marka_sell = input("Melyik autót kívánja eladni? ")
                auto_elad(marka_sell)

            elif usr_int == 5:
                flag = False
            # else:
            #     print("Kérjük válaszon a menüpontok közül: \n 1. Kocsi felvetel. \n 2. Osszes kocsi adatai lekerdezese \n
            #     3. Kocsi adatainak lekerdezese index alapjan. \n 4. Kocsi eladasa\n 5. Kilépés")
        except ValueError:
            print("Kérjük számot adj meg!")


marka_list = ["skoda", "skoda", "dacia", "audi"]
kor_list = [4, 5, 3, 2]
start()

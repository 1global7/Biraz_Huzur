import time, sys

def slow_print(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

soru = "bos"
cvp = 0
end = False
havuc = "0"
donus = "0"

slow_print("Bu sabah da gürültüyle uyandım.\n")

while end == False:

    while soru == "bos":
        print(" 1 - Yataktan kalk\n 2 - Yatmaya devam et")
        cvp = input("> ")

        if cvp == "1":
            slow_print ("Yataktan kalktım\n")
            soru = "ytkodası"
        elif cvp == "2":
            slow_print ("Bu gürültüde uyumanın mümkünatı yok.\n")
            soru = "bos"
        else:
            print ("Hiçbirşey yapmamak bir seçenek değil -Malesef-")

    while soru == "ytkodası":
        slow_print("Salondan bazı sesler geliyor.\n")
        print(" 1 - Banyoya git\n 2 - Salona git")
        cvp = input("> ")

        if cvp == "1":
            slow_print ("Kapı kitli.\n")
            soru = "ytkodası"
        elif cvp == "2":
            soru = "salongrs"
        else:
            print ("Hiçbirşey yapmamak bir seçenek değil -Malesef-")

    while soru == "salongrs":
        if donus == "0":slow_print("Üçlü kanepenin üzerinde bir at oturuyor.\n-Kişneme sesleri-\nSesin kaynağını buldum sanırım.\n")
        if donus == "1":slow_print("-Kişneme sesleri-\n")
        print(" 1 - Atın yanına git\n 2 - Mutfağa git\n 3 - Balkona git")
        cvp = input("> ")

        if cvp == "1":
            donus = "1"
            soru = "atmhbbt"
        elif cvp == "2":
            donus = "1"
            soru = "mtfk"
        elif cvp == "3":
            donus = "1"
            soru = "blkn"
        else:
            print ("Hiçbirşey yapmamak bir seçenek değil -Malesef-")

    while soru == "atmhbbt":
        slow_print("Atın yanına yaklaştım.\n")
        if havuc == "0":print(" 1 - :Hey sen de kimsin ?\n 2 - :Kişnemeyi kes ve defol evimden!\n 3 - Geri dön")
        if havuc == "1":print(" 1 - Havucu ata ver\n 2 - :Kişnemeyi kes ve defol evimden!\n 3 - Geri dön")
        cvp = input("> ")

        if cvp == "1" and havuc == "0":
            slow_print ("-Kişneme sesleri-\n")
            slow_print ("Sanırım aç\n")
        elif cvp == "1" and havuc == "1":
            slow_print ("Havucu ata verdim.\n")
            slow_print ("At sustu.\n")
            soru = "huzur"
        elif cvp == "2":
            slow_print ("-Daha yüksek kişneme sesleri-\n")
            slow_print ("Sanırım bu işe yaramadı\n")
        elif cvp == "3":
            soru = "salongrs"
        else:
            print ("Hiçbirşey yapmamak bir seçenek değil -Malesef-")

    while soru == "mtfk":
        slow_print("Etrafta birkaç hamamböceği dolaşıyor.\n")
        print(" 1 - Dolaba bak\n 2 - Su iç\n 3 - Salona dön")
        cvp = input("> ")

        if cvp == "1":
            slow_print ("Sulanmış yoğurt dışında birşey yok.\n")
        elif cvp == "2":
            slow_print ("Su yerine çamur akıyor.\n")
        elif cvp == "3":
            soru = "salongrs"
        else:
            print ("Hiçbirşey yapmamak bir seçenek değil -Malesef-")

    while soru == "blkn":
        if havuc == "0":slow_print("Dışarıda fırtına var\n")
        print(" 1 - Balkon kapısını aç\n 2 - Salona geri dön")
        cvp = input("> ")

        if cvp == "1" and havuc == "0":
            slow_print ("Dışarısı buz gibi ama yerde bir havuç buldum.\n")
            havuc = "1"
        elif cvp == "1" and havuc == "1":
            slow_print ("Dışarısı buz gibi.\n")
        elif cvp == "2":
            soru = "salongrs"
        else:
            print ("Hiçbirşey yapmamak bir seçenek değil -Malesef-")

    while soru == "huzur":
        slow_print ("Sonunda biraz huzur.\n")
        slow_print ("Bitti.\n")
        sys.exit()
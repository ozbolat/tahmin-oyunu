game_front = []
game_back = []
gamers = {}
point = 0
def close_letter(c):
    c = c - 1
    a = str('')
    game_front[c] = a
    return game_front[c]

def open_letter(c):
    if game_front[c-1] == '':
        game_front[c-1] = game_back[c-1]

def change_letters(a,b):
    a = a - 1
    b = b - 1
    h = game_front[b]
    game_front[b] = game_front[a]
    game_front[a] = h
    j = game_back[b]
    game_back[b] = game_back[a]
    game_back[a] = j
winner_list = open("winner_list.txt","w")
while (True):

    print("""
    **********************
    1 - ) Oyuna BAŞLA
    2 - ) Nasıl Oynanır?
    3 - ) Kazananların listesi
    4 - ) Çıkış
    **********************
    """)
    choice = int(input(""))
    if choice == 4:
        break
    if choice == 2:
        print("""
    2 kişiyle oynan bir hafıza oyunudur. Oyunun amacı en sondaki harf dizilimini doğru 
    bilmek. 
    Sırasıyla toplam 6 değer olmak üzere harf veya rakam girerek oyuna başlanır. 
    Her tur 3 seçenek sunulur. 1. seçenek olan değer kapatma ile sırası gelen oyuncu 
    -eğer en az 1 tane açık değer varsa- kapatmak istediği değerin sırasını yazar. 
    2. seçenek olan değer açma ile sırası gelen oyuncu -eğer en az 1 tane kapalı değer varsa- 
    açmak istediği değerin sırasını yazar. 3. seçenek olan 2 değerin yerini değiştirme ile belirttiği
    2 değerin yerlerini değiştirir. 5. turun sonunda tahmin hakkı tanınır. Kabul edilirse sırası gelen
    oyuncu tahmin eder. Tahmin doğruysa kendisi, tahmin doğru değilse rakibi oyunu kazanır. Kabul 
    edilmezse sıra diğer oyuncuya geçer ve oyun devam eder.
        """)
    if choice == 3:
        winner_list = open("winner_list.txt","r")
        print(winner_list.read())
    if choice == 1:
        player1 = input("1. oyuncunun adı: ")
        gamers.setdefault(player1,point)
        player2 = input("2. oyuncunun adı: ")
        gamers.setdefault(player2,point)
        game_back.clear()
        game_front.clear()
        point = 0
        i = 0
        q = 0
        sayac = 0
        while (i < 6):
            i = i + 1
            if i % 2 == 0:
                x = input(f"{player2} harf veya rakam girin: ")
            else:
                x = input(f"{player1} harf veya rakam girin: ")
            x = x.upper()
            if game_front.count(x) > 0 or x == "" or len(x) > 1:
                i = i - 1
                print("Yanlış değer girdiniz! Lütfen farklı bir değer giriniz.")
            else:
                game_front.append(x)
                game_back.append(x)

        while(q < 10):  
            q = q + 1
            print(game_front)
            sayac = sayac + 1
            if sayac % 2 == 1:
                print(f"\n{player1} sıra sizde!\n")
            else:
                print(f"\n{player2} sıra sizde!\n")
            print("""İşlem Seçiniz
            1 - Değer Kapatma
            2 - Değer Açma
            3 - 2 Değerin Yerini Değiştirme""")
            i = int(input(""))
            if i == 1:
                if game_front.count("") < 6:
                    z = int(input("Kaçıncı değeri kapatacağınızı seçiniz: "))
                    close_letter(z)
                else:
                    sayac = sayac - 1
                    q = q - 1
                    print("Açık bir değer bulunamamıştır! Lütfen başka bir eylem seçiniz.")
            elif i == 2:
                if game_front.count("") > 0:
                    z = int(input("Kaçıncı değeri açacağınızı seçiniz: "))
                    open_letter(z)
                else:
                    sayac = sayac - 1
                    q = q - 1
                    print("Kapalı bir değer bulunamamıştır! Lütfen başka bir eylem seçiniz.")
            elif i == 3:
                v = int(input("Kaçıncı değeri değiştirmek istiyorsunuz: "))
                b = int(input("Kaçıncı değerle değiştirmek istiyorsunuz: "))
                change_letters(v,b)
            if q == 10:
                print(game_front)
                f = int(input("Tahmin etmek istiyorsanız 1'e basın: "))
                if f == 1:
                    for i in range(6):
                        n = input(f"{i+1}. değer: ")
                        n = n.upper()
                        if n == game_back[i]:
                            continue
                        else:
                            break
                    if i == 5:
                        if sayac % 2 == 1:
                            print(game_back)
                            print(f"{player1} Oyunu Kazandı!")
                            gamers[player1] = gamers[player1] + 1
                            gamers.update({player1: gamers[player1]})
                            winner_list.write(f"{player1}: {gamers[player1]}")
                            
                        else:
                            print(game_back)
                            print(f"{player2} Oyunu Kazandı!")
                            gamers[player2] = gamers[player2] + 1
                            gamers.update({player2: gamers[player2]})
                            winner_list.write(f"{player2}: {gamers[player2]}")
                            
                    else:
                        if sayac % 2 == 1:
                            print(game_back)
                            print(f"{player1} yanlış tahmin ettiği için {player2} Oyunu Kazandı!")
                            gamers[player2] = gamers[player2] + 1
                            gamers.update({player2: gamers[player2]})
                            winner_list.write(f"{player2}: {gamers[player2]}")
                            
                        else:
                            print(game_back)
                            print(f"{player2} yanlış tahmin ettiği için {player1} Oyunu Kazandı!")
                            gamers[player1] = gamers[player1] + 1
                            gamers.update({player1: gamers[player1]})
                            winner_list.write(f"""{player1}: {gamers[player1]}""")

                else:
                    q = q - 1
winner_list.close()









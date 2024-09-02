fayl_adi = 'C:\\Users\\YourName\\Documents\\metn.txt'  # Burada fayl yolunu öz sisteminizə uyğun dəyişin

try:
    with open(fayl_adi, 'r') as fayl:
        metn = fayl.read()
        sozler = metn.split()
        soz_sayi = len(sozler)
    print("Faylda", soz_sayi, "söz var.")
except FileNotFoundError:
    print(f"'{fayl_adi}' faylı tapılmadı. Zəhmət olmasa faylın adını və yerini yoxlayın.")

#tap 2
with open('eskifayl.txt', 'r') as fayl:
    icindekiler = fayl.read()

with open('yenifayl.txt', 'w') as fayl:
    fayl.write(icindekiler)

print("Fayl uğurla kopyalandı.")

#tap3
soz = input("Axtarmaq istədiyiniz sözü daxil edin: ")
say = 0

with open('metn.txt', 'r') as fayl:
    for setir in fayl:
        say += setir.count(soz)

print(f"Söz '{soz}' faylda {say} dəfə təkrarlanır.")

# tap4
soz = input("Hansı sözü olan sətirləri silmək istəyirsiniz? ")

with open('metn.txt', 'r') as fayl:
    setirler = fayl.readlines()

with open('metn.txt', 'w') as fayl:
    for setir in setirler:
        if soz not in setir:
            fayl.write(setir)

print("İstənilən sətirlər silindi.")

# tap5
cemi = 0

with open('metn.txt', 'r') as fayl:
    for setir in fayl:
        sozler = setir.split()
        for soz in sozler:
            if soz.isdigit():
                cemi += int(soz)

print("Fayldakı rəqəmlərin cəmi:", cemi)

# tap 5
with open('eskifayl.txt', 'r') as fayl:
    setirler = fayl.readlines()

with open('ters_fayl.txt', 'w') as fayl:
    for setir in setirler:
        fayl.write(setir[::-1])

print("Məlumatlar tərsinə çevrilmiş fayla yazıldı.") 
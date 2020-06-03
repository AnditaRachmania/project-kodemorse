# # Lat 1:

# def dengan return function
# kalkulator (+, =, :, *)
# inputan:
# input angka 1: 8
# input angka 2 : 10
# masukkan operator: +

# def calc(x, y, z):
#     if z == '+':
#         return x + y
#     elif z == '-':
#         return x - y
#     elif z == '*':
#         return x * y
#     elif z == '/':
#         return x/y
#     else:
#         return 'Operator tidak tersedia'

# try:
#     angka1 = int(input('Masukkan angka: '))
#     angka2 = int(input('Masukkan angka: '))
#     simbol = input("Pilih operator (+, - , *, /) : ")
#     hasil = calc(angka1, angka2, simbol)
#     print(f'Hasil dari {angka1} {simbol} {angka2} = {hasil}')
# except:
#     print('Hanya menerima bilangan integer')


# # Lat 2
# pake dictionary dan def:
# kamus IND - ENG untuk hari

# Translator (encoder - decoder kode morse)
# silahkan masukkan kalimat: Aman
# outputnya: (kode morsenya) * - / - - / * - / - *

# silahkan masukkan kalimat: * - / - - / * - / - *
# output: Aman

# >> otomatis berubah, ga perlu ada pilihan translate dari A ke B atau dari B ke A

alfanum = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']

# dictionary dari alfanum - morse
alf_morse = {}

for alf, code in zip(alfanum, morse):
    alf_morse[alf] = code

# dictionary dari morse - alfanum
mors_alf = {}

for code, alf in zip(morse, alfanum):
    mors_alf[code] = alf


# fungsi kamus kode morse ke alfanumerik
def morsetoalfnum():
    pecah = kata.split('/')
    for i in pecah:
        trans = mors_alf.get(i)
        print(trans.upper(), end='')
    print()
        

def alfnumtomorse():
    listkata = list(kata)
    for i in listkata:
        trans = alf_morse.get(i)
        print(trans + '/', end='')
    print()
        

greet = 'ENCODER - DECODER KODE MORSE'
print('='* len(greet))
print(greet)
print('='* len(greet))


menu = True
while menu:
    print('Menu: \n1. ENCODER/DECODER \n2. EXIT')
    print()
    try:
        pilih = int(input('Pilih menu [1/2]:'))
        print()
        if pilih == 1:
            kata = input("Masukkan kata (gunakan '/' untuk memisahkan karakter kode morse): ")   
            kata = kata.lower()
            cekkata = kata.isalnum()
            if cekkata == True:
                print('Alfanumerik to Morse')
                alfnumtomorse()
                menu = True
            else:
                print('Morse to Alfanumerik')
                morsetoalfnum()
                menu = True
        elif pilih == 2:
            print('** TERIMAKASIH **')
            menu = False
        else:
            print('Input salah')
            menu = True
    except:
        print('Input Salah')


# # Lat 3
# Fizz Buzz
# input: masukkan angka:
# output
# angka yang habis bisa dibagi 3: Fizz
# angka yang habis bisa dibagi 5 : Buzz
# angka yang habis bisa dibagi 3 dan dibagi 5 : Fizz Buzz

# def ganti(a, b):
#     for i in range(a, b):
#         if i%15 == 0:
#             print('FizzBuzz')
#         elif i%3 == 0:
#             print('Fizz')
#         elif i%5 == 0:
#             print('Buzz')
#         else:
#             print(i)

# loop = True
# while loop:
#     a = int(input('Masukkan nilai batas bawah: '))
#     b = int(input('Masukkan nilai batas atas:'))

#     ganti(a, b)
#     print()
#     konfirm = input('Lagi [Y/N]? ')
#     print()
#     konfirm = konfirm.lower()
#     if konfirm == 'y':
#         loop = True
#     elif konfirm == 'n':
#         print('** TERIMAKASIH **')
#         loop = False
#     else:
#         print('Input salah')
#         loop = True


# # Lat 4
# pake def:
# caesar cipher
# masukkan kata: Joni
# masukkan angka: 2
# hasil caesar cipher: lnpk (tiap huruf ditambah 2 selisihnya)

# alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# def caesar(kata, num):
#     list_kata = list(kata)
#     for i in list_kata:
#         idx = alfabet.index(i) + num
#         akhir = idx % 26
#         katabaru = alfabet[akhir]
#         print(katabaru, end='')
#     print()
    
      
# loop = True
# while loop:
#     kata = input('masukkan kata: ')
#     num = int(input('masukkan angka: '))
#     caesar(kata, num)
#     konfirm = input('Lagi [Y/N]? ')
#     print()
#     konfirm = konfirm.lower()
#     if konfirm == 'y':
#         loop = True
#     elif konfirm == 'n':
#         print('** TERIMAKASIH **')
#         loop = False
#     else:
#         print('Input salah')
#         loop = True


# # lat 5
# pake def dan dict:
# batasin maksimal 4000 di luar itu keluar notif: angka di luar jangkauan
# translator (encoder-decoder angka romawi)
# silahkan masukkan angka: 2018
# output: MMXVIII

# latin = ['1','4','5','9','10','40','50','90','100','400','500','900','1000']
# romawi = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']

# # dict latin - roman
# lat_rom = {}
# for lat, rom in zip(latin, romawi):
#     lat_rom[lat] = rom

# # print(lat_rom)

# # convert = lat_rom.get('1000')
# # print(convert)

# # dict roman - latin
# rom_lat = {}
# for rom, lat in zip(romawi, latin):
#     rom_lat[rom] = lat
# # print(rom_lat)

# # def latintoroman(angka):

# num = int(input('Masukkan angka latin: '))
# ribu = num // 1000 * 1000
# sisaribu = num % 1000
# ratus = sisaribu // 100 * 100
# sisaratus = sisaribu % 100
# puluh = sisaratus // 10 * 10
# satuan = sisaratus % 10

# lengkap = .join(ribu, ratus, puluh, satuan)


# convert = lat_rom.get(ribu)
# print(convert)
# for i in lengkap:
#     convert = rom_lat.get(i)
# print(lengkap)
# menu = True
# while menu:
#     angka = input("Masukkan Angka Romawi/Latin: ")
#     cek1 = angka.isalnum():
#     # cek angka masih dalam rentang/tidak
#     if cek1 == True:
#         cek2 = angka.isnumeric()
#         if cek2 == True:
#             print("ANGKA LATIN >> ANGKA ROMAWI")
#             # fungsi latintoroman
#             menu = True
#         else:
#             print("ANGKA ROMAWI >> ANGKA LATIN")
#             # fungsi romantolatin
#             menu = True
#     else:
#         print("Input yang Anda masukkan bukan Angka Latin/Romawi")
#         menu = True


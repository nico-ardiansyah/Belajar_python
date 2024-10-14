""" Latihan Operasi AND"""

print ("Latihan Pertama Operasi Boolean\n")
angka1 = int(input("Masukan Angka Pertama : "))

hasilAngka1 = angka1 > 0
hasilAngka2 = angka1 < 5
hasilAngka3 = angka1 > 8
hasilAngka4 = angka1 < 11

hasil1 = hasilAngka1 and hasilAngka2
hasil2 = hasilAngka3 and hasilAngka4
hasil3 = (hasilAngka1 and hasilAngka2) or (hasilAngka3 and hasilAngka4)

print (f"Hasil Pertama = {hasil1}")
print (f"Hasil Kedua = {hasil2}")
print(f"Hasil perbandingan : {hasil3}")

""" Latihan Operasi AND Dan OR """

print ("Latihan Kedua Operasi Boolean\n")
angka2 = int(input("Masukan Angka Pertama : "))

hasil4 = angka2 < 0
hasil5 = angka2 > 5
hasil6 = angka2 < 8
hasil7 = angka2 >11

hasilA = hasil4 or hasil5
hasilB = hasil6 or hasil7
hasilD = (hasil4 or hasil5) and (hasil6 or hasil7) 

print(f"Hasil Pertama = {hasilA}")
print(f"Hasil Kedua = {hasilB}")
print(f"Seluruh Hasil = {hasilD}")
"""Mangambil input dari user"""

print("===Tipe input String===")
String = input("Masukan Nama: ")

print("Data : ", String,"bertipe ",type(String))

print("===Tipe input Integer===")
Integer = int(input("Masukan Angka Interger (bilangan bulat): "))

print("Data : ", Integer,"bertipe ",type(Integer))

print("===Tipe input Float===")
Float = float(input("Masukan Angka Float (bilangan desimal): "))

print("Data : ", Float,"bertipe ",type(Float))

print("===Tipe input Boolean===")
"""Untuk tipe data booean untuk value True / Flase maka harus
di casting terlebih dahulu ke dalam interger, dan diubah menjadi
boolean"""
Boolean = bool(int(input("Masukan Angka Boolean: ")))

print("Data : ", Boolean,"bertipe ",type(Boolean))



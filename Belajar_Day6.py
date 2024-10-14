""" Operasi Aritmatika """

a = 5
b = 2

#Penjumlahan
print ("Penjumlahan")
penjumlahan = a + b
print(a,"+",b,"=",penjumlahan)

#Pengurangan
print ("Pengurangna")
pengurangan = a - b
print(a,"-",b,"=",pengurangan)

#Pembagian
print ("Pembagian")
pembagian = a / b
print(a,"/",b,"=",pembagian)

#Perkalian
print ("Perkalian")
perkalian = a * b
print(a,"*",b,"=",perkalian)

#Eksponen (pemangkatan)
print ("Eksponen (Pemangkatan)")
pemangkatan = a ** b
print(a,"**",b,"=",pemangkatan)

#Modulus (sisa dari hasil pembagian)
print ("Modulus (sisa dari hasil pembagian")
modulus = a % b
print(a,"%",b,"=",modulus)

#Floor division (pembulatan kebawah dari pembagian)
print ("Floor division (pembulatan kebawah dari pembagian")
FlorDivision = a // b
print(a,"//",b,"=",FlorDivision)

#Operasi preceedence
""" 
urutan operasi yang dikerjakan komputer 
1. Tanda Kurung ()
2. eksponen **
3. Perkalian *, Pembagian /, Floor division //, Modulus %
4. Penjumlahan +, Pengurangan -
"""
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x 
print (x,"**",y,"*",z,"+",x,"/",y,"-",y,"%","z","//",x,"=",hasil)
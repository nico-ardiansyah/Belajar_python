""" Operasi Komparasi """
""" Opersi Komparasi akan selalu menghasilkan nilai True/False"""

a = 4
b = 2

#Lebih besar dari (>)
#Operasi (>) akan mulai dihitung setelah dari titik yang ditentukan
print ("Operasi Lebih Besar Dari (>)")
hasil = a > 5
print (a,">",5,"=",hasil)
hasil = b > 2
print (b,">",2,"=",hasil)
hasil = a > b
print (a,">",b,"=",hasil)

#Kurang dari (<)
#Operasi (<) akan mulai dihitung sebelum dari titik yang ditentukan
print ("Operasi Lebih Kecil Dari (<)")
hasil = a < 5
print (a,"<",5,"=",hasil)
hasil = b < 2
print (b,"<",2,"=",hasil)
hasil = a < b
print (a,"<",b,"=",hasil)


#Kurang dari sama dengan (<=)
#Operasi (<=) akan mulai dihitung dari titik yang ditentukan
print ("Operasi Lebih Kecil Dari Sama Dengan (<=)")
hasil = a <= 5
print (a,"<=",5,"=",hasil)
hasil = b <= 2
print (b,"<=",2,"=",hasil)
hasil = a <= b
print (a,"<=",b,"=",hasil)

#Lebih dari sama dengan (>=)
#Operasi (>=) akan mulai dihitung dari titik yang ditentukan
print ("Operasi Lebih Besar Dari Sama Dengan (>=)")
hasil = a <= 5
print (a,"<=",5,"=",hasil)
hasil = b <= 2
print (b,"<=",2,"=",hasil)
hasil = a <= b
print (a,"<=",b,"=",hasil)

#sama dengan (==)
#Operasi (==) membandingkan 2 variabel atau 2 nilai
print ("Operasi Sama Dengan (==)")
hasil = a == 5
print (a,"==",5,"=",hasil)
hasil = b == 2
print (b,"==",2,"=",hasil)
hasil = a == b
print (a,"==",b,"=",hasil)

#tidak sama dengan (!=)
#Operasi (!=) membandingkan 2 variabel atau 2 nilai
print ("Operasi Tidak Sama Dengan (!=)")
hasil = a != 5
print (a,"!=",5,"=",hasil)
hasil = b != 2
print (b,"!=",2,"=",hasil)
hasil = a != b
print (a,"!=",b,"=",hasil)

#is (is)
#Operasi (is) membandingkan 2 variabel (objek/memori sementara)
#Jika yang dibandikan adalah variabel dengan value maka akan warning
#Hasil True jika a sama dengan b
print ("Operasi is (is)")
hasil = a is b
print ("a is b =",hasil)

#isnot (is not)
#Operasi (is not) membandingkan 2 variabel (objek/memori sementara)
#Jika yang dibandikan adalah variabel dengan value maka akan warning
#Hasil True jika a tidak sama dengan b
print ("Operasi is not (is not)")
hasil = a is not b
print ("a is not b =",hasil)


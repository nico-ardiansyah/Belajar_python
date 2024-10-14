""" Operasi Logika Boolean """

""" Operasi NOT """

print ("Operasi NOT")
#jika bukan True maka hasilnya False
#jika bukan False maka True
a = False 
b = not a
print ("Data a:",a)
print ("Not a : ", b)


print ("\nOperasi OR")
#Jika salah True maka hasilnya True
a = False 
b = False 
c = a or b
print (a,' OR',b,':',c)
a = True 
b = True 
c = a or b
print (a,'  OR',b,' :',c)
a = True 
b = False 
c = a or b
print (a,'  OR',b,':',c)
a = False 
b = True  
c = a or b
print (a,' OR',b,' :',c)

print ("\nOperasi AND")
#Jika kedua nilai adalah True maka hasilnya True
a = False 
b = False 
c = a and b
print (a,' AND',b,':',c)
a = True 
b = True 
c = a and b
print (a,'  AND',b,' :',c)
a = True 
b = False 
c = a and b
print (a,'  AND',b,':',c)
a = False 
b = True  
c = a and b
print (a,' AND',b,' :',c)

print ("\nOperasi XOR")
#Jika kedua nilai adalah True / False maka hasilnya adaah False
a = False 
b = False 
c = a ^ b
print (a,' XOR',b,':',c)
a = True 
b = True 
c = a ^ b
print (a,'  XOR',b,' :',c)
a = True 
b = False 
c = a ^ b
print (a,'  XOR',b,':',c)
a = False 
b = True  
c = a ^ b
print (a,' XOR',b,' :',c)


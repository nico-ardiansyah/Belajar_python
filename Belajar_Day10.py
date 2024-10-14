""" Belajar Operasi Bitwise """

print (" Belajar Operasi Bitwise\n")

a = 5
b = 6

#Operator or (|)
print ("====== OR ======")
print (f" nilai a : {a} , binarynya : ", format (a,'08b'))
print (f" nilai b : {b} , binarynya : ", format (b,'08b'))
c = a | b
print (f"{a} | {b} = {c}")
print (f"binary {c} : ",format(c,'08b'))



#Operator and (&)
print ("\n====== AND ======")
print (f" nilai a : {a} , binarynya : ", format (a,'08b'))
print (f" nilai b : {b} , binarynya : ", format (b,'08b'))
c = a & b
print (f"{a} & {b} = {c}")
print (f"binary {c} : ",format(c,'08b'))


#Operator XOR (^)
print ("\n====== XOR ======")
print (f" nilai a : {a} , binarynya : ", format (a,'08b'))
print (f" nilai b : {b} , binarynya : ", format (b,'08b'))
c = a ^ b
print (f"{a} ^ {b} = {c}")
print (f"binary {c} : ",format(c,'08b'))

#Operator left shifting (>>)
print ("\n====== LEFT SHIFTING ======")
print (f" nilai a : {a} , binarynya : ", format (a,'08b'))
c = a >> 2
print (f"{a} >> 2 = {c}")
print (f"binary {c} : ",format(c,'08b'))

#Operator right shifting (>>)
print ("\n====== RIGHT SHIFTING ======")
print (f" nilai a : {a} , binarynya : ", format (a,'08b'))
c = a << 2
print (f"{a} << 2 = {c}")
print (f"binary {c} : ",format(c,'08b'))

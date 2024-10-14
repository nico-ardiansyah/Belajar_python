"""Belajar Casting type data (merubah tipe data)"""
"""Tipe data boolean akan bernilai False apabila bilangannya = 0,
dan apabila selain 0 (nol) maka bernilai True"""

print("====Data Integer====")
Integer = 10
print("Data : ", Integer, "bertipe", type(Integer))
print("Integer menjadi float")
Float = float(Integer)
print("Data : ", Float, "bertipe", type(Float))
print("Integer menjadi string")
String = str(Integer)
print("Data : ", String, "bertipe", type(String))
print("Integer menjadi Boolean")
Boolean = bool(Integer)
print("Data : ", Boolean, "bertipe", type(Boolean))

print("====Data Float====")
Float = 11.9
print("Data : ", Float, "bertipe", type(Float))
print("Float menjadi Integer")
"""Tipe data Float jika diubah ke tipe data int maka akan selalu
dibulatkan kebawah"""
Integer = int(Float)
print("Data : ", Integer, "bertipe", type(Integer))
print("Float menjadi string")
String = str(Float)
print("Data : ", String, "bertipe", type(String))
print("Float menjadi Boolean")
Boolean = bool(Float)
print("Data : ", Boolean, "bertipe", type(Boolean))

print("====Data String====")
"""Tipe data string jika dirubah menjadi int, float, boolean
akan error jika valuenya bertipe huruf (abc...) dan akan
tidak error kalau tipenya angka ("10")"""
String = "10"
print("Data : ", String, "bertipe", type(String))
print("String menjadi Integer")
Integer = int(String)
print("Data : ", Integer, "bertipe", type(Integer))
print("String menjadi Float")
Float = float(String)
print("Data : ", Float, "bertipe", type(Float))
print("String menjadi Boolean")
"""jika merubah tipe data string menjadi boolean, untuk mendapatkan
value False maka data string harus kosong ("")"""
Boolean = bool(String)
print("Data : ", Boolean, "bertipe", type(Boolean))

print("====Data Boolean====")
Boolean = False
print("Data : ", Boolean, "bertipe", type(Boolean))
print("Boolean menjadi Integer")
Integer = int(Boolean)
print("Data : ", Integer, "bertipe", type(Integer))
print("Boolean menjadi String")
String = str(Boolean)
print("Data : ", String, "bertipe", type(String))
print("Boolean menjadi Float")
Float = float(Boolean)
print("Data : ", Float, "bertipe", type(Float))


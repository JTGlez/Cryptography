import fileinput
 
suma = 0
suma2 = 0

for f in fileinput.input():
    suma = suma + int(f)

print(suma)

for g in fileinput.input():
    suma2 = suma2 + float(g)

print(suma)
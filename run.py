import fileinput
 
suma = 0

for f in fileinput.input():
    suma = suma + f

print(suma)
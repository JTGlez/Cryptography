import fileinput
 
suma = 0

for f in fileinput.input():
    if '.' in f:
        suma = suma + float(f)
    else:
        suma = suma + int(f)

print(suma)
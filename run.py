import fileinput
 
suma = 0
suma2 = 0

def es_numero(str):
    if str.replace('.', '').isdigit():
        return int(str)
    else:
        return float(str)

for f in fileinput.input():
    suma = suma + es_numero(f)

print(suma)
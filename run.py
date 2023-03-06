import fileinput
 
suma = 0

def es_numero(str):
    if str.replace('.', '').isdigit():
        return int(str)
    elif str.replace('.', '', 1).isdigit():
        return float(str)
    else:
        print("No es válido")

for f in fileinput.input():
    suma = suma + es_numero(f)

print(suma)
import fileinput

lines = []

for line in fileinput.input():
    lines.append(line)

a = input()
b = input()

c = a + b

def suma ():
    return a + b
    
print(suma())

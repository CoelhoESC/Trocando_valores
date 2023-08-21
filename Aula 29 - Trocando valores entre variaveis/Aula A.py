"""
Trocando o valor entre variaveis
"""
x = 10
y = 'Everton'

# Para invertir:
x, y = y, x
print(f'x={x} e y={y}')

# Pode ser feito com mais variavel:
x = 10
y = 'Everton'
z = 5.25
x, y, z = z, x, y
print(f'x={x}, y={y}, z={z}')

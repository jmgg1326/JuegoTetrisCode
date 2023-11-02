class Tetromino:
    def __init__(self, matrix):
        self.matrix = matrix

    def rotar(self):
        rotado = []
        for i in range(len(self.matrix[0])):
            rotado.append([])
            for j in range(len(self.matrix) - 1, -1, -1):
                rotado[i].append(self.matrix[j][i])
        self.matrix = rotado

    def __str__(self):
        resultado = ""
        for fila in self.matrix:
            resultado += ''.join(['.' if celda != '@' else '@' for celda in fila]) + '\n'
        return resultado

    def iguales(self, otro):
        return self.matrix == otro.matrix

    def similares(self, otro):
        for i in range(4):
            if self.iguales(otro):
                return True
            otro.rotar()
        return False

# Ejemplo de uso
T = Tetromino([
    ['.', '.', '.'],
    ['.', '@', '@'],
    ['@', '@', '.']
])

print("T después de dos rotaciones:")
print(T)
T.rotar()
T.rotar()
print(T)

Z = Tetromino([
    ['.', '.', '.'],
    ['@', '@', '.'],
    ['.', '@', '@']
])

print("Z en su estado original:")
print(Z)

print("¿T y Z son iguales?", T.iguales(Z))
print("¿T y Z son similares?", T.similares(Z))

# Matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Exibindo a matriz formatada
print("Matriz 3x3:")
for linha in matriz:
    print(" | ".join(f"{elemento:^3}" for elemento in linha))

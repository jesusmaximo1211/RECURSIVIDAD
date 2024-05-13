
def romano_a_decimal(num_romano):
    
    valores_romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if not num_romano:
        return 0

    if len(num_romano) == 1:
        return valores_romanos[num_romano]

    if valores_romanos[num_romano[0]] < valores_romanos[num_romano[1]]:
        return valores_romanos[num_romano[1]] - valores_romanos[num_romano[0]] + romano_a_decimal(num_romano[2:])
    else:
        return valores_romanos[num_romano[0]] + romano_a_decimal(num_romano[1:])

print(romano_a_decimal('IX'))



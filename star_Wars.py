def usar_la_fuerza(mochila, indice=0, objetos_sacados=0):
    if indice >= len(mochila):
        print("No se encontró un sable de luz en la mochila.")
        return False, objetos_sacados
    
    if mochila[indice] == "sable de luz":
        print("hay un sable de luz")
        return True, objetos_sacados + 1
    
    print("el jedi saca:", mochila[indice])
    return usar_la_fuerza(mochila, indice + 1, objetos_sacados + 1)


mochila = ["pistola", "botiquín", "sable de luz", "ropa", "juguete"]
encontrado, objetos_sacados = usar_la_fuerza(mochila)
if encontrado:
    print("Se necesitaron", objetos_sacados, "objetos para encontrar el sable de luz.")

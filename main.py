from datos import conteos

if __name__ == "__main__":
    resultados = conteos()
    if resultados:
        for tabla, filas in resultados:
            print(f"{tabla}: {filas}")
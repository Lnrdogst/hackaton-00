def calculate() -> float:
    while True:
        expr = input("Escribe una suma (o 'c' para borrar): ").strip()
        if expr == 'c':
            print("Operación borrada.")
            continue
        if expr == "":
            raise ValueError("Empty expression")

        try:
            # Elimina espacios extras
            expr = expr.replace(" ", "")
            # Verifica que solo contiene dígitos, + y puntos
            for ch in expr:
                if not (ch.isdigit() or ch == '+' or ch == '.'):
                    raise ValueError("Invalid character")

            # Separa por el operador +
            partes = expr.split('+')
            suma = 0.0
            for parte in partes:
                if parte == "":
                    raise SyntaxError("Syntax error in sum")
                suma += float(parte)
            print("Resultado:", suma)
            return suma
        except ValueError:
            print("Error: Caracter inválido")
            raise
        except SyntaxError:
            print("Error: Sintaxis inválida")
            raise
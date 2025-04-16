def calculate() -> float:
    while True:
        expr = input("Escribe una operación con + y - (o 'c' para borrar): ").strip()
        if expr == 'c':
            print("Operación borrada.")
            continue
        if expr == "":
            raise ValueError("Empty expression")

        try:
            expr = expr.replace(" ", "")
            if any(c not in "0123456789.+-" for c in expr):
                raise ValueError("Invalid character")

            # Convierte la expresión a una lista de números y operadores
            tokens = []
            i = 0
            while i < len(expr):
                if expr[i] in '+-':
                    if i == 0 or expr[i-1] in '+-':
                        num = expr[i]
                        i += 1
                        while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                            num += expr[i]
                            i += 1
                        tokens.append(num)
                    else:
                        tokens.append(expr[i])
                        i += 1
                elif expr[i].isdigit() or expr[i] == '.':
                    num = ''
                    while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                        num += expr[i]
                        i += 1
                    tokens.append(num)
                else:
                    raise ValueError("Invalid character")

            # Evaluar suma y resta
            result = float(tokens[0])
            i = 1
            while i < len(tokens):
                op = tokens[i]
                num = float(tokens[i+1])
                if op == '+':
                    result += num
                elif op == '-':
                    result -= num
                else:
                    raise SyntaxError("Invalid operator")
                i += 2

            print("Resultado:", result)
            return result
except ZeroDivisionError:
            print("Error: División por cero")
            raise
        except ValueError:
            print("Error: Caracter inválido")
            raise
        except SyntaxError:
            print("Error: Sintaxis inválida")
            raise
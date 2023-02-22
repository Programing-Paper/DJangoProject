def numericos(*args):
    resultado = 0
    for suma in args:
        resultado += suma
        
        
    return resultado


print(f'el resultado es {numericos(10, 20, 30, 40)}')

def multiplicacion(*args):
    resultado = 1
    for suma in args:
        resultado *= suma 
        
        
    return resultado


print(f'el resultado es {multiplicacion(10, 20, 30, 40, 50)}')

def listarterminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listarterminos(IDE='Integrated Development Eviroment', PK='Primary key')
listarterminos(DBMS='Database Management System')

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)

resultado = factorial(5)
print(f'el resultado es: {resultado}')

def recursiva(valor):
    if valor >= 1:
        print(valor)
        recursiva(valor - 1)
    elif valor == 0:
        return 
    elif valor <= 0:
        print('valor incorrecto...')

recursiva(5)

# Ejersicio calculadora de impuestos

# sinimpuesto = int(input('Proporcione el pago sin impuesto: '))
# montoimpuesto = int(input('Proporcione el monto del impuesto: '))

# print(sinimpuesto, montoimpuesto)





    

    
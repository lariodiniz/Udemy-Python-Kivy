#coding: utf-8
"""

try:
    a = 10 / 0
    print(a)
except ZeroDivisionError:
    print("Não é possivel dividir o número por zero.")


def input_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Número inválido")

num1 = input_float("Digite o primeiro numero: ")
num2 = input_float("Digite o segundo numero: ")

while True:
    try:
        print(num1/num2)
        break
    except ZeroDivisionError:
        print("Não é possivel dividir o número por zero.")
        num2 = input_float("Digite o segundo numero: ")
"""
def erro(x):
    try:
        eval(x)
    except ValueError as e:
        print("ValueError")
        print(type(e))
        print(e.args)
        print(e)
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except (TypeError,NameError) as e:
        print(type(e))        
    else:
        print("Nenhuma exceção ocorreu.")
    finally:
         print("Sempre será executado.")


#TypeError
erro("int+int")

#NameError
erro("a")

#ValueError
erro("int('a')")

#ZeroDivisionError
erro("5/0")
erro("10+10")

print("A aplicação foi finalizada.")

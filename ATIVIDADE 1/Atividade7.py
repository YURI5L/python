n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
opera = input("Digite uma operação")

if opera == "+":
   print("Soma: " , n1+n2)

elif opera == "-":
   print("Subtração: " , n1-n2)

elif opera == "*":
   print("Multiplicação: " , n1*n2)

elif opera == "/":
   print("Divisão: " , n1/n2)


else:
   print("Operação Invalida")

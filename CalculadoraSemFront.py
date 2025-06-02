print("SIMULADOR DE JUROS COMPOSTOS \n")
print("Para números decimais utilize (.), Não utilize (,).\n")

capital = float(input("Digite qual é o seu capital: R$ "))
periodo = str(input("A taxa de juros e o tempo será em meses ou em anos? (Responda (M) para mensal ou (A) para anual): "))

if periodo.upper() == "M":
  juros_porcentagem = float(input("Digite qual é a taxa de juros mensal: % "))
  tempo = int(input("Digite por quanto meses o seu dinheiro ficará aplicado: "))

  juros = juros_porcentagem / 100

elif periodo.strip() == "a":
  juros_porcentagem = float(input("Digite qual é a taxa de juros anual: % "))
  tempo = int(input("Digite por quanto anos o seu dinheiro ficará aplicado: "))

  #Fórmula da taxa equivalente
  juros = (1 + (juros_porcentagem / 100))**(1/12) - 1

  tempo *= 12

else:
  print("\nInfelizmente ocorreu algum erro, leia atentamente as instruções para preencher as informações e recomece a operação!")
  exit()

aporte = float(input("Digite o seu aporte mensal: R$ "))

montante = capital

print("\nResumo da evolução mês a mês:\n")
print("Mês\tMontante (R$)")

for i in range(tempo + 1):
  if i == 0:
    print(f"{i}\t{montante:.2f}")
  else:
    montante = (montante + aporte) * (1 + juros)
    print(f"{i}\t{montante:.2f}")

print(f"\nO seu montante final é: R$ {montante:.2f}")
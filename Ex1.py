def soma_ate(indice):

  soma = 0
  k = 0 
  for k in range(0, indice + 1):
    soma += k
  return soma
  
resultado = soma_ate(13)
print("O valor da variavél SOMA é:", resultado)


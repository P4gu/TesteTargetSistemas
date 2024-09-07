def inverter_string(string):
 
    string_invertida = ""
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

minha_string = "Obrigada pelo desafio!"
resultado = inverter_string(minha_string)
print(resultado)
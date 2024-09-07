def calcular_percentual_estados(faturamento_estados):

    faturamento_total = sum(faturamento_estados.values())
    percentuais = {}
    for estado, valor in faturamento_estados.items():
        percentuais[estado] = (valor / faturamento_total) * 100
    return percentuais

#dados
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

#percentuais
resultados = calcular_percentual_estados(faturamento)

#resultados
for estado, percentual in resultados.items():
    print(f"{estado}: {percentual:.2f}%")
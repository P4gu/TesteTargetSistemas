import json

def analisar_faturamento(arquivo):

    with open(arquivo, 'r') as f:
        dados = json.load(f)

    faturamentos = [dado['valor'] for dado in dados if dado['valor'] > 0]

    if not faturamentos:
        return None, None, 0

    menor_valor = min(faturamentos)
    maior_valor = max(faturamentos)
    media = sum(faturamentos) / len(faturamentos)
    dias_acima_media = sum(1 for valor in faturamentos if valor > media)

    return media, menor_valor, maior_valor, dias_acima_media


arquivo = 'Ex3P\dados.json' 
media, menor, maior, dias_acima = analisar_faturamento(arquivo)

if menor is not None:
    print(f"A media do faturamento deste mês: R${media:.2f}")
    print(f"Menor valor de faturamento: R$ {menor:.2f}")
    print(f"Maior valor de faturamento: R$ {maior:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima}")
else:
    print("Não há dados de faturamento válidos.")

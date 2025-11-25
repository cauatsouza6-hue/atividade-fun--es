def aplicar_desconto(valor, desconto):
    return valor - desconto

def calcular_total(valor, frete):
    return valor + frete

def formatar_moeda(valor):
    return f"R$ {valor:.2f}".replace('.', ',')
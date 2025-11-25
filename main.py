import funcoes

print("""
=============================
      SISTEMA DE CAIXA
=============================
1 - Aplicar desconto
2 - Somar frete
3 - Sair
""")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    valor = float(input("Digite o valor da compra: R$ "))
    desconto = float(input("Digite o valor do desconto: R$ "))
    resultado = funcoes.aplicar_desconto(valor, desconto)
    print("Valor final:", funcoes.formatar_moeda(resultado))
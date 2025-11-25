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

elif opcao == 2:
    valor = float(input("Digite o valor da compra: R$ "))
    frete = float(input("Digite o valor do frete: R$ "))
    resultado = funcoes.calcular_total(valor, frete)
    print("Valor total:", funcoes.formatar_moeda(resultado))

elif opcao == 3:
    print("Saindo do sistema...")

else:
    print("Opção inválida!")

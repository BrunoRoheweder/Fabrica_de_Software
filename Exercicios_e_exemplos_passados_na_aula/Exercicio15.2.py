preco = float(input("Digite o valor do pão: "))
for pao in range (1,51):
    arm = pao * 0.18
    print(f"\nQuantidade de pães: {pao}\nValor: {preco*arm}")
    print("\nQuantidade de pães: %f \nValor: %f "%(pao,preco*arm))
    

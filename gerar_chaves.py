# gerar_chaves.py

from utils import eh_primo, gerar_primo, calcular_mdc, calcular_inverso_modular

print("=== GERADOR DE CHAVES RSA ===")

escolha = input("Deseja inserir os primos manualmente? (s/n): ")

# Escolha dos primos
if escolha == 's':
    p = int(input("Digite o valor de p: "))
    q = int(input("Digite o valor de q: "))

    # Validação dos primos
    if not eh_primo(p) or not eh_primo(q):
        print("Erro: p e q precisam ser primos!")
        exit()

    if p == q:
        print("Erro: p e q não podem ser iguais!")
        exit()

else:
    p = gerar_primo()
    q = gerar_primo()

    while p == q:
        q = gerar_primo()

    print(f"Primos gerados automaticamente: p={p}, q={q}")

# Cálculo de n
n = p * q

# Cálculo do phi
phi = (p - 1) * (q - 1)

# Escolha do e (coprimo com phi)
e = 3
while calcular_mdc(e, phi) != 1:
    e += 1

# Cálculo da chave privada d
d = calcular_inverso_modular(e, phi)

# Exibição das chaves
print("\n=== CHAVES GERADAS ===")
print(f"Chave Pública (n, e): ({n}, {e})")
print(f"Chave Privada (n, d): ({n}, {d})")
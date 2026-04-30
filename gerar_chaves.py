# gerar_chaves.py 

from utils import eh_primo, gerar_primo, calcular_mdc, calcular_inverso_modular

print("=== GERADOR DE CHAVES RSA ===")

escolha = input("Deseja inserir os primos manualmente? (s/n): ")

# Escolha dos primos
if escolha.lower() == 's':
    while True:
        try:
            p = int(input("Digite o valor de p: "))
            q = int(input("Digite o valor de q: "))

            if not eh_primo(p) or not eh_primo(q):
                print("❌ Erro: p e q precisam ser números primos.")
                continue

            if p == q:
                print("❌ Erro: p e q não podem ser iguais.")
                continue

            if (p * q) < 128:
                print("❌ Erro: n muito pequeno para ASCII.")
                continue

            break

        except ValueError:
            print("❌ Erro: Digite apenas números inteiros.")

else:
    while True:
        p = gerar_primo()
        q = gerar_primo()

        if p != q:
            n = p * q

            # garante que n é grande o suficiente
            if n >= 256:
                break

    print(f"Primos gerados automaticamente: p={p}, q={q}")

# Agora calcula tudo uma vez só
n = p * q
phi = (p - 1) * (q - 1)

# Escolha de e
e = 3
while e < phi:
    if calcular_mdc(e, phi) == 1:
        break
    e += 1

# Cálculo do d
d = calcular_inverso_modular(e, phi)

if d is None:
    print("Erro ao calcular d.")
    exit()

# Exibição
print("\n=== CHAVES GERADAS ===")
print(f"Chave Pública (n, e): ({n}, {e})")
print(f"Chave Privada (n, d): ({n}, {d})")
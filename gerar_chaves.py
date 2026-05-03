from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.prompt import Prompt
from utils import eh_primo, gerar_primo, calcular_mdc, calcular_inverso_modular
# gerar_chaves.py 

console = Console()

def gerar_chaves():
    console.print(Panel.fit(Align.center("=== GERADOR DE CHAVES RSA ==="), title="Gerador de Chaves RSA", title_align="center", border_style="green"), justify="center")

    escolha = Prompt.ask("Deseja inserir os primos manualmente? (s/n): ")

    # Escolha dos primos
    if escolha.lower() == 's':
        while True:
            try:
                p = int(Prompt.ask("Digite o valor de p: "))
                q = int(Prompt.ask("Digite o valor de q: "))

                if not eh_primo(p) or not eh_primo(q):
                    console.print(Panel.fit(Align.center("❌ Erro: p e q precisam ser números primos."), border_style="red"), justify="center")
                    continue

                if p == q:
                    console.print(Panel.fit(Align.center("❌ Erro: p e q não podem ser iguais."), border_style="red"), justify="center")
                    continue

                if (p * q) < 128:
                    console.print(Panel.fit(Align.center("❌ Erro: n muito pequeno para ASCII."), border_style="red"), justify="center")
                    continue

                break

            except ValueError:
                console.print(Panel.fit(Align.center("❌ Erro: Digite apenas números inteiros."), border_style="red"), justify="center")

    else:
        while True:
            p = gerar_primo()
            q = gerar_primo()

            if p != q:
                n = p * q

                # garante que n é grande o suficiente
                if n >= 256:
                    break

        console.print(Panel.fit(Align.center(f"Primos gerados automaticamente: p={p}, q={q}"), border_style="green"), justify="center")

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
        console.print(Panel.fit(Align.center("❌ Erro ao calcular d."), border_style="red"), justify="center")
        exit()

    # Exibição
    console.print(Panel.fit(Align.center(f"\nChave Pública (n, e): ({n}, {e})\nChave Privada (n, d): ({n}, {d})"), border_style="green", title='=== CHAVES GERADAS ==='), justify="center")
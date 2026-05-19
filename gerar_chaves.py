from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.prompt import Prompt
from utils import eh_primo, gerar_primo, calcular_mdc, calcular_inverso_modular
import json
import os
# gerar_chaves.py 

console = Console()

def confirmar(prompt_text: str, max_attempts: int | None = None, default: bool | None = None) -> bool:
    """Lê uma resposta de confirmação aceitando variações de 'sim' e 'não'.

    - Usa `casefold()` para aceitar maiúsculas e variantes Unicode.
    - `max_attempts`: se fornecido, após N respostas inválidas retorna `default` ou lança `ValueError`.
    - `default`: valor retornado quando `max_attempts` é excedido (se None, levanta erro).
    """
    yes = {'s', 'sim', 'y', 'yes'}
    no = {'n', 'nao', 'não', 'no'}
    attempts = 0

    while True:
        resposta = Prompt.ask(prompt_text).strip().casefold()
        attempts += 1

        if resposta in yes:
            return True
        if resposta in no:
            return False

        console.print(Panel.fit(Align.center("Resposta inválida. Digite 's'/'sim' ou 'n'/'não'."), border_style="red"), justify="center")

        if max_attempts is not None and attempts >= max_attempts:
            if default is not None:
                return default
            raise ValueError(f"Número máximo de tentativas excedido para: {prompt_text}")

def gerar_chaves():
    console.print(Panel.fit(Align.center("=== GERADOR DE CHAVES RSA ==="), title="Gerador de Chaves RSA", title_align="center", border_style="green"), justify="center")

    # Escolha dos primos
    if confirmar("Deseja inserir os primos manualmente? (s/n): "):
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
    console.print(Panel.fit(Align.center("Escolha de e"), border_style="blue"), justify="center")
    entrada_e = confirmar("Deseja inserir e manualmente? (s/n): ")
    
    if entrada_e:
        while True:
            try:
                e = int(Prompt.ask("Digite o valor de e: "))
                
                # Validações de e
                if e <= 1 or e >= phi:
                    console.print(Panel.fit(Align.center(f"❌ Erro: e deve estar entre 2 e {phi-1}"), border_style="red"), justify="center")
                    continue
                
                if calcular_mdc(e, phi) != 1:
                    console.print(Panel.fit(Align.center(f"❌ Erro: gcd(e, phi) deve ser 1!\n👉 e={e} e phi={phi} não são coprimos"), border_style="red"), justify="center")
                    continue
                
                break
            except ValueError:
                console.print(Panel.fit(Align.center("❌ Erro: Digite apenas números inteiros."), border_style="red"), justify="center")
    else:
        # Geração automática de e
        e = 3
        while e < phi:
            if calcular_mdc(e, phi) == 1:
                break
            e += 1

    # Cálculo do d
    d = calcular_inverso_modular(e, phi)

    if d is None:
        console.print(Panel.fit(Align.center("❌ Erro ao calcular d."), border_style="red"), justify="center")
        return

    #  SALVAR CHAVES EM ARQUIVO
    chaves = {
        "p": p,
        "q": q,
        "n": n,
        "phi": phi,
        "e": e,
        "d": d,
        "chave_publica": [n, e],
        "chave_privada": [n, d]
    }
    
    # Salva em arquivo JSON
    with open("chaves.json", "w") as arquivo:
        json.dump(chaves, arquivo, indent=4)
    
    # Exibição
    console.print(Panel.fit(Align.center(f"\n✅ Chaves geradas com sucesso!\n\n" + 
                                        f"p = {p}\nq = {q}\n\n" +
                                        f"n = {n}\nphi(n) = {phi}\n\n" +
                                        f"e = {e}\nd = {d}\n\n" +
                                        f"Chave Pública (n, e): ({n}, {e})\n" +
                                        f"Chave Privada (n, d): ({n}, {d})\n\n" +
                                        f"💾 Chaves salvas em 'chaves.json'"), 
                           border_style='green', title='=== CHAVES GERADAS ==='), justify="center")
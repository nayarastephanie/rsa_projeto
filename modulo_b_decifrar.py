# modulo_b_decifrar.py
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.align import Align
from time import sleep
console = Console()
import os
continuar = True

def descifrar():
  if (continuar == True):
    while True:  
        console.print(Panel.fit(Align.center("=== MÓDULO B - DECIFRAR ==="), border_style='green'), justify='center')
        sleep(2)

        # 📂 Listar arquivos disponíveis (.rsa)
        arquivos = [f for f in os.listdir() if f.endswith(".rsa")]

        if not arquivos:
            console.print(Panel.fit(Align.center("❌ Nenhum arquivo .rsa encontrado."), border_style='red'), justify='center')
            break

        console.print(Panel.fit(Align.center("Arquivos disponíveis:"), border_style='green'), justify='center')
        for arquivo in arquivos:
            console.print(Panel.fit(Align.center(f"- {arquivo}"), border_style='green'), justify='center')

        # Usuário escolhe o arquivo
        nome_arquivo = Prompt.ask("\nDigite o nome do arquivo (ex: mensagem1.rsa): ")

        # Entrada da chave privada
        try:
            n = int(Prompt.ask("Digite o valor de n: "))
            d = int(Prompt.ask("Digite o valor de d: "))
        except ValueError:
            console.print(Panel.fit(Align.center("❌ Erro: n e d devem ser números inteiros."), border_style='red'), justify='center')
            break

        # Leitura do arquivo escolhido
        try:
            with open(nome_arquivo, "r") as arquivo:
                conteudo = arquivo.read()
        except FileNotFoundError:
            console.print(Panel.fit(Align.center("❌ Erro: arquivo não encontrado."), border_style='red'), justify='center')
            break   

        # Verifica se está vazio
        if not conteudo.strip():
            console.print(Panel.fit(Align.center("❌ Erro: arquivo vazio."), border_style='red'), justify='center')
            break

        # Converte para lista
        numeros = conteudo.split()

        mensagem_original = ""

        # Descriptografia
        for numero in numeros:
            try:
                numero = int(numero)
            except ValueError:
                console.print(Panel.fit(Align.center("❌ Erro: conteúdo inválido no arquivo."), border_style='red'), justify='center')
                break

            decifrado = pow(numero, d) % n

            try:
                mensagem_original += chr(decifrado)
            except ValueError:
                console.print(Panel.fit(Align.center("❌ Erro ao converter número para caractere."), border_style='red'), justify='center')
                break

        # Exibe resultado
        console.print(Panel.fit(Align.center("Mensagem descriptografada:"), border_style='green'), justify='center')
        console.print(Panel.fit(Align.center(mensagem_original), border_style='green'), justify='center')
        sleep(2)


        console.print(Panel.fit(Align.center(f"Quantidade de caracteres decifrados: {len(numeros)}"), border_style='green'), justify='center')
        sleep(1)
        continuar == False
        return
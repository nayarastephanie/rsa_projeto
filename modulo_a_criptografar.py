# modulo_a_criptografar.py
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.align import Align
import os


console = Console()

continuar = True

#Função se encontra gerando um loop infinito
def criptografar():
  
  if (continuar == True):
    while True:
        console.print(Panel.fit(Align.center("=== MÓDULO A - CRIPTOGRAFAR ==="), border_style='green'), justify='center')

        # Entrada da mensagem
        mensagem = Prompt.ask("Digite a mensagem: ")
    
        
        if not mensagem:
                console.print(Panel.fit(Align.center("❌ Erro: a mensagem não pode estar vazia."), border_style='red'), justify='center')
            
                break
            # Entrada da chave pública
        try:
                n = int(Prompt.ask("Digite o valor de n: "))
                e = int(Prompt.ask("Digite o valor de e: "))
        except ValueError:
                console.print(Panel.fit(Align.center("❌ Erro: n e e devem ser números inteiros."), border_style='red'), justify='center')
                break

        mensagem_criptografada = []

            # Validação do tamanho de n
        for caractere in mensagem:
            if ord(caractere) >= n:
                console.print(Panel.fit(Align.center("❌ Erro: n é muito pequeno para os caracteres da mensagem."), border_style='red'), justify='center')
                console.print(Panel.fit(Align.center("👉 Gere chaves maiores."), border_style='red'), justify='center')
                break
###############################################################
        #Aprovado
        # Criptografia
        for caractere in mensagem:
            
            numero = ord(caractere)
            
            cifrado = pow(numero, e) % n
            
            mensagem_criptografada.append(cifrado)

        # Exibe resultado
        console.print(Panel.fit(Align.center("Mensagem criptografada:"), border_style='green'), justify='center')
        console.print(mensagem_criptografada)

        console.print(Panel.fit(Align.center(f"Quantidade de caracteres criptografados: {len(mensagem_criptografada)}"), border_style='green'), justify='center')



        contador = 1

        # Procura um nome disponível
        while os.path.exists(f"mensagem{contador}.rsa"):
            contador += 1

        nome_arquivo = f"mensagem{contador}.rsa"

        # Salva em arquivo .rsa
        with open(nome_arquivo, "w") as arquivo:
            arquivo.write(" ".join(map(str, mensagem_criptografada)))

        console.print(Panel.fit(Align.center(f"Arquivo '{nome_arquivo}' gerado com sucesso!"), border_style='green'), justify='center')
        continuar == False
        return
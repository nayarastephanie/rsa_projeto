# modulo_a_criptografar.py
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.align import Align
from utils import calcular_mdc
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
            continue
        
        # Entrada da chave pública
        try:
                n = int(Prompt.ask("Digite o valor de n: "))
                e = int(Prompt.ask("Digite o valor de e: "))
        except ValueError:
                console.print(Panel.fit(Align.center("❌ Erro: n e e devem ser números inteiros."), border_style='red'), justify='center')
                continue
        
        #  VALIDAÇÕES CRÍTICAS
        # Verifica se n >= 128 (mínimo para ASCII)
        if n < 128:
            console.print(Panel.fit(Align.center(f"❌ ERRO: n={n} é muito pequeno!\n👉 n deve ser >= 128"), border_style='red'), justify='center')
            continue
        
        # Verifica se e > 1 e e < n
        if e <= 1 or e >= n:
            console.print(Panel.fit(Align.center(f"❌ ERRO: e inválido!\n👉 e deve estar entre 2 e {n-1}\n👉 e = {e} não é válido"), border_style='red'), justify='center')
            continue

        mensagem_criptografada = []
        
        #  VALIDAÇÃO: Todos os caracteres devem ser menores que n
        caractere_invalido = False
        for caractere in mensagem:
            if ord(caractere) >= n:
                console.print(Panel.fit(Align.center(f"❌ ERRO: Caractere '{caractere}' (ASCII {ord(caractere)}) >= n={n}\n👉 Gere chaves maiores."), border_style='red'), justify='center')
                caractere_invalido = True
                break
        
        if caractere_invalido:
            continue
        # ✅ CRIPTOGRAFIA
        for caractere in mensagem:
            numero = ord(caractere)
            cifrado = pow(numero, e, n)  # Exponenciação modular eficiente!
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
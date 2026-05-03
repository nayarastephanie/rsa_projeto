from modulo_a_criptografar import criptografar
from modulo_b_decifrar import descifrar
from rich.panel import Panel
from rich.align import Align
from rich.console import Console
from time import sleep
from gerar_chaves import gerar_chaves
console = Console()


console.print(Panel.fit(Align.center('Bem vindo ao sistema de criptografia RSA!'), title='Trabalho de Segurança da Informação', title_align='center', border_style='green'), justify='center')
sleep(2)   

def main():
   while True: 
        console.print(Panel.fit(Align.center('Escolha uma das seguinte opções: \n1. Gerar novas chaves\n2. Criptografar mensagem\n3. Decifrar mensagem\n4.Encerrar programa'), border_style='green'), justify='center')
        escolha = console.input("\nDigite o número da opção desejada: ")
        match escolha:
                case '1':
                    gerar_chaves()
                case '2':
                    criptografar()
                case '3':
                    descifrar()
                case '4':
                    console.print(Panel.fit(Align.center('Programa encerrado.'), border_style='green'), justify='center'
    )
                    exit()


if __name__ == "__main__":    main()
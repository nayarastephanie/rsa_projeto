# Projeto RSA - Criptografia

## 📌 Objetivo
Implementar o algoritmo RSA com dois módulos independentes:
- Módulo A: Criptografia
- Módulo B: Descriptografia

---

## ⚙️ Funcionalidades

### 🔑 Geração de Chaves
- Permite inserir números primos manualmente
- Ou gerar automaticamente
- Valida se os números são primos
- Gera:
  - Chave pública (n, e)
  - Chave privada (n, d)

---

### 🔒 Módulo A - Criptografar
- Entrada: texto (UTF-8)
- Usa tabela ASCII (função ord)
- Saída: números criptografados
- Salva em arquivo `.rsa`

---

### 🔓 Módulo B - Decifrar
- Lê arquivo `.rsa`
- Usa chave privada
- Converte números para texto (chr)
- Exibe mensagem original

---

## 🧠 Implementação

O algoritmo RSA foi implementado manualmente, sem uso de bibliotecas prontas de criptografia.

Foram utilizadas:
- Operações matemáticas básicas
- Aritmética modular
- Geração de números primos
- Funções nativas do Python (ord e chr)

---

## ⚠️ Restrições atendidas

- Não utiliza bibliotecas RSA prontas
- Código autoral
- Uso de inteiros grandes
- Módulos separados

---

## 👨‍💻 Observação

A conversão de caracteres foi feita utilizando ASCII, permitindo suportar:
- Letras
- Números
- Espaços
- Símbolos

---

## 📂 Arquivos

- gerar_chaves.py → gera as chaves
- modulo_a_criptografar.py → criptografa
- modulo_b_decifrar.py → descriptografa
- utils.py → funções auxiliares

---

## 🚀 Execução

1. Execute gerar_chaves.py
2. Execute modulo_a_criptografar.py
3. Execute modulo_b_decifrar.py
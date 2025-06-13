import math
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_quiz():
    score = 0

    print("Bem-vindo ao Quiz de Raciocínio Matemático!")
    print("Complete as lacunas do código e entenda as restrições matemáticas.")
    print("---------------------------------------------------")

    # Questão 1
    print("\nQuestão 1:")
    print("if _____________:")
    print("    resultado = (a + b) / (c - d)")
    print("    print('Resultado:', resultado)")
    print("else:")
    print("    print('O denominador não pode ser ____________.')")
    print("a) c == d | zero")
    print("b) c != d | negativo")
    print("c) a + b == 0 | nulo")
    answer = input("Sua resposta (a, b ou c): ").lower()
    if answer == 'b':
        print("Correto!")
        score += 1
    else:
        print("Incorreto. A resposta correta é 'b'.")
    input("Pressione Enter para continuar...")    
    limpar_tela()

    # Questão 2
    print("\nQuestão 2:")
    print("if _____________:")
    print("    resultado = ((x * y) - z)**0.5")
    print("    print('Resultado:', resultado)")
    print("else:")
    print("    print('O radicando não pode ser ____________.')")
    print("a) (x * y) - z > 0 | zero")
    print("b) (x * y) - z >= 0 | negativo")
    print("c) x * y > z | par")
    answer = input("Sua resposta (a, b ou c): ").lower()
    if answer == 'b':
        print("Correto!")
        score += 1
    else:
        print("Incorreto. A resposta correta é 'b'.")
    input("Pressione Enter para continuar...")  
    limpar_tela()  

    # Questão 3
    print("\nQuestão 3:")
    print("if _____________:")
    print("    resultado = math.log(a**2 - b)")
    print("    print('Resultado:', resultado)")
    print("else:")
    print("    print('O argumento do logaritmo deve ser ____________.')")
    print("a) a**2 - b > 0 | positivo")
    print("b) a**2 - b != 0 | inteiro")
    print("c) a**2 > b | racional")
    answer = input("Sua resposta (a, b ou c): ").lower()
    if answer == 'a':
        print("Correto!")
        score += 1
    else:
        print("Incorreto. A resposta correta é 'a'.")
    input("Pressione Enter para continuar...")  
    limpar_tela()  

    # Questão 4
    print("\nQuestão 4:")
    print("if _____________:")
    print("    resultado = (m + n) / (p + q)")
    print("    print('Resultado:', resultado)")
    print("else:")
    print("    print('O denominador não pode ser ____________.')")
    print("a) p + q > 0 | negativo")
    print("b) p + q != 0 | zero")
    print("c) p e q inteiros | nulo")
    answer = input("Sua resposta (a, b ou c): ").lower()
    if answer == 'b':
        print("Correto!")
        score += 1
    else:
        print("Incorreto. A resposta correta é 'b'.")
    input("Pressione Enter para continuar...")  
    limpar_tela()  

    # Questão 5
    print("\nQuestão 5:")
    print("if _____________:")
    print("    resultado = (u - v)**0.5")
    print("    print('Resultado:', resultado)")
    print("else:")
    print("    print('O radicando não pode ser ____________.')")
    print("a) u - v > 0 | zero")
    print("b) u - v % 2 == 0 | ímpar")
    print("c) u - v >= 0 | negativo")
    answer = input("Sua resposta (a, b ou c): ").lower()
    if answer == 'c':
        print("Correto!")
        score += 1
    else:
        print("Incorreto. A resposta correta é 'c'.")
    input("Pressione Enter para continuar...")
    limpar_tela()  

    # Questão 6
    print("\nQuestão 6:")
    print("if _____________:")
    print("    resultado = math.log(r * s)")
    print("    print('Resultado:', resultado)")
    print("else:")
    print("    print('O argumento do logaritmo deve ser ____________.')")
    print("a) r * s > 0 | positivo")
    print("b) r * s != 0 | não-nulo")
    print("c) r e s reais | racional")
    answer = input("Sua resposta (a, b ou c): ").lower()
    if answer == 'a':
        print("Correto!")
        score += 1
    else:
        print("Incorreto. A resposta correta é 'a'.")
    input("Pressione Enter para continuar...")
    limpar_tela()  

    # Questão 7
    print("\nQuestão 7:")
    print("if _____________:")
    print("    resultado = 10 / ((e + f) - (g * h))")
    print("    print('Resultado:', resultado)")
    print("else:")
    print("    print('O denominador não pode ser ____________.')")
    print("a) (e + f) - (g * h) > 0 | negativo")
    print("b) (e + f) - (g * h) != 0 | zero")
    print("c) (e + f) - (g * h) inteiro | irracional")
    answer = input("Sua resposta (a, b ou c): ").lower()
    if answer == 'b':
        print("Correto!")
        score += 1
    else:
        print("Incorreto. A resposta correta é 'b'.")
    input("Pressione Enter para continuar...")
    limpar_tela()  

    # Questão 8
    print("\nQuestão 8:")
    print("if _____________:")
    print("    resultado = (x**2 - y**2)**0.5")
    print("    print('Resultado:', resultado)")
    print("else:")
    print("    print('O radicando não pode ser ____________.')")
    print("a) x**2 - y**2 > 0 | par")
    print("b) x**2 - y**2 % 2 == 0 | ímpar")
    print("c) x**2 - y**2 >= 0 | negativo")
    answer = input("Sua resposta (a, b ou c): ").lower()
    if answer == 'c':
        print("Correto!")
        score += 1
    else:
        print("Incorreto. A resposta correta é 'c'.")
    input("Pressione Enter para continuar...")  
    limpar_tela()  

    # Questão 9
    print("\nQuestão 9:")
    print("if _____________:")
    print("    resultado = math.log(abs(k - l) - m)")
    print("    print('Resultado:', resultado)")
    print("else:")
    print("    print('O argumento do logaritmo deve ser ____________.')")
    print("a) abs(k - l) - m > 0 | positivo")
    print("b) abs(k - l) - m != 0 | diferente de zero")
    print("c) abs(k - l) - m real | inteiro")
    answer = input("Sua resposta (a, b ou c): ").lower()
    if answer == 'a':
        print("Correto!")
        score += 1
    else:
        print("Incorreto. A resposta correta é 'a'.")
    input("Pressione Enter para continuar...")
    limpar_tela()  

    # Questão 10
    print("\nQuestão 10:")
    print("if _____________:")
    print("    resultado = (-27)**(1/3)")
    print("    print('Resultado:', resultado)")
    print("else:")
    print("    print('A operação é válida, pois é possível calcular a raiz ____________ de número ____________.')")
    print("a) True | cúbica | negativo")
    print("b) False | quadrada | positivo")
    print("c) (-27) > 0 | cúbica | real")
    answer = input("Sua resposta (a, b ou c): ").lower()
    if answer == 'a':
        print("Correto!")
        score += 1
    else:
        print("Incorreto. A resposta correta é 'a'.")
    input("Pressione Enter para continuar...")
    limpar_tela()  

    print("\n---------------------------------------------------")
    print(f"Quiz finalizado! Você acertou {score} de 10 questões.")

if __name__ == "__main__":
    while True:
        run_quiz()
        repetir = input("\nDeseja tentar o quiz novamente? (s/n): ").lower()
        if repetir != 's':
            print("Obrigado por jogar! Até a próxima!")
            break
        limpar_tela()

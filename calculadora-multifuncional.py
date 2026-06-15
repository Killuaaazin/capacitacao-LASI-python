def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: divisão por zero"
    return x / y
def conservacao_energia(trabalho_realizado, energia_inicial):
    energia_final = energia_inicial - trabalho_realizado
    return energia_final
def calculo_da_posição_da_queda_projetil(velocidade_inicial, angulo, tempo):
    import math
    angulo_rad = math.radians(angulo)
    posicao_x = velocidade_inicial * math.cos(angulo_rad) * tempo
    posicao_y = velocidade_inicial * math.sin(angulo_rad) * tempo - (0.5 * 9.81 * tempo ** 2)
    return posicao_x, posicao_y

def calculadora():
    print("=== Calculadora Básica ===")
    while True:
        print("\nOperações:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Conservação de Energia")
        print("6. Cálculo da Posição de Queda de um Projétil")
        print("7. Sair")
        
        opcao = input("\nEscolha uma operação (1/2/3/4/5/6): ")
        
        if opcao == "7":
            print("Encerrando a calculadora...")
            break
        
        if opcao in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                if opcao == "1":
                    resultado = somar(num1, num2)
                    print(f"{num1} + {num2} = {resultado}")
                elif opcao == "2":
                    resultado = subtrair(num1, num2)
                    print(f"{num1} - {num2} = {resultado}")
                elif opcao == "3":
                    resultado = multiplicar(num1, num2)
                    print(f"{num1} * {num2} = {resultado}")
                elif opcao == "4":
                    resultado = dividir(num1, num2)
                    print(f"{num1} / {num2} = {resultado}")  
                       
            except ValueError:
                print("Erro: Digite números válidos!")
        elif opcao == "5":
            try:
                trabalho_realizado = float(input("Digite o trabalho realizado (em Joules): "))
                energia_inicial = float(input("Digite a energia inicial (em Joules): "))
                resultado = conservacao_energia(trabalho_realizado, energia_inicial)
                print(f"Energia final: {resultado} Joules")
            except ValueError:
                print("Erro: Digite números válidos!")
                
        elif opcao == "6":
            try:
                velocidade_inicial = float(input("Digite a velocidade inicial (em m/s): "))
                angulo = float(input("Digite o ângulo de lançamento (em graus): "))
                tempo = float(input("Digite o tempo de voo (em segundos): "))
                posicao_x, posicao_y = calculo_da_posição_da_queda_projetil(velocidade_inicial, angulo, tempo)
                print(f"Posição X: {posicao_x:.2f} metros")
                print(f"Posição Y: {posicao_y:.2f} metros")
                
            except ValueError:
                print("Erro: Digite números válidos!")
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    calculadora()

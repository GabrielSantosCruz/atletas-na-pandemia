#/*******************************************************************************
#Autor: Gabriel Santos Cruz
#Componente Curricular: Algoritmos I
#Concluido em: xx/xx/2021
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#******************************************************************************************/

# Entrada de dados:
print("Sistema UEFS pelos atletas\n")

rep = 's'
quant = 0
# Se eu digitar um numero em vez de uma string e dar erro?

while rep.lower() == 's':
    quant += 1

    while True:
        try:
            age = int(input("Digite sua idade: "))
            break
        except ValueError:
            print("Erro! Digite a idade em números! ")
            continue

    gender = input("Digite seu sexo (M/F): ")
    fever = input("Teve febre (S/N): ")

    if fever.lower() == 's':
        temperatura = float(input("Qual foi a maior temperatura detectada: "))

    else:
        symp_quant = 0
        symp_quant += 1
        symptom = input("Teve algum sintoma (S/N): ")

    kit = input("Tomou o kit Covid ao retornar ao Brasil (S/N): ")

    medal = input("Ganhou alguma medalha? (S/N): ")
    
# Calcular a quantidade de medalhas e qual o seu tipo (Ouro, Prata, Bronze)

    if medal.lower() == 's':

        gold = int(input("Quantas medalhas de ouro?: "))
        silver = int(input("Quantas medalhas de prata?: "))
        bronze = int(input("Quantas medalhas de bronze?: "))
    
    rep = input("Deseja cadastrar um novo atleta?(S/N): ")

    if rep.lower() == 'n':

        print("O cadastramento foi encerrado!!!")

# Processamento de dados:
percent_symp = float((100 * symp_quant) / quant) # procentagem dos sintomáticos


# Saída de dados:
   
    # Quantidade de atletas monitorados;
print(f"A quantidade de atletas monitorados é de {quant}!")

    # A quantidade e a porcentagem de atletas que apresentaram sintomas;

print(f"A quantidade de atletas que apresentam sintomas é de {symp_quant}.\n O que equivale a {percent_symp}% do total!" )

    # Idade média de todos os atletas, dos atletas sem sintomas, e dos atletas sintomáticos;
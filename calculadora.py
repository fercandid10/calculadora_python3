from time import sleep
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-= CALCULADORA BÁSICA -=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print()
sleep(2)  # Import da biblioteca sleep apenas para um charme/frescurinha na aplicacao

totalizando = 0  #Variavel faz interação com a variavel total e outras, variavel de auxilio
total = 0        #Variavel que recebe o primeiro resultado da calculadora a op_parcial
resp = 1         #Variavel para a condição

while True:
    aux = 0 #Variavel auxiliar
    op_parcial = 0  #Variavel que recera o primeiro resultado da operacao

    n1 = float(input("Informe um valor: ")) #Primeiro valor
    sinal = str(input("Informe o sinal da operação [+ , -, *, /, %] : ")) #Sinal para operação
    n2 = float(input("Informe outro valor: ")) #Segundo valor

    if sinal == "+":           #Condições
        soma = n1 + n2 #OP de adiçao
        aux = soma  #aux recebe valor de soma

    if sinal == "-":
        sub = n1 - n2  #OP de subtracao
        aux = sub  #aux recebe valor de sub

    if sinal == "*":
        multi = n1 * n2   #Op de multiplicacao
        aux = multi   #aux recebe valor de multi

    if sinal == "/":
        divi = n1 / n2  #Op de divisao
        aux = divi #aux recebe valor de divisao


    op_parcial += aux #Op_parcial recebe o valor inicial mais o valor de aux | op_parcial = op_parcial + aux
    total = op_parcial #Total recebe o valor de op_parcial

    resp = int(input("Digite 1 p/ Continuar ou 2 p/ Sair: ")) #variavel de condicao

    if resp == 2: #Igual
        print(f"O total foi {total}") #Mostra o total na tela, caso a escolha seja Sair
        break #Finaliza o programa

    if resp != 2: #Diferente
        while resp!= 2:

            sinal = str(input("Informe o sinal da operação [+ , -, *, /, %] : "))
            continuando = float(input("Informe o valor: ")) #Valor para  sequencial do calculo


            if sinal == "+":
                total += totalizando #Em primeiro momento prevalece o valor de total, totalizando tem valor zero.
                soma1 = total + continuando #Variavel recebe o valor de total, soma, pelo novo valor de sequencia

                print()
                print(soma1) #Mostra o resultado
                resp = int(input("Digite 1 p/ Continuar ou 000 p/ ENCERRAR: ")) #Variavel de condicao
                if resp == 000:
                    print('BYE')
                    exit(000) #Pequena gambiarra que finaliza o programa

                total = soma1 #Total passa a ser o valor de soma1
                totalizando = soma1 #Totalizando passa a ser o valor de soma1
                total = 0  # zera-se a variavel total

            if sinal == "-":
                total += totalizando #Em primeiro momento prevalece o valor de total, totalizando tem valor zero.
                sub1 = total - continuando  #Variavel recebe o valor de total, subtrai, pelo novo valor de sequencia

                print()
                print(sub1)
                resp = int(input("Digite 1 p/ Continuar ou 000 p/ ENCERRAR: "))
                if resp == 000:
                    print('BYE')
                    exit(000)

                total = sub1
                totalizando = sub1
                total = 0


            if sinal == "*":
                total += totalizando #Em primeiro momento prevalece o valor de total, totalizando tem valor zero.
                multiplicar = total * continuando #Variavel recebe o valor de total, multiplica, pelo novo valor de sequencia

                print()
                print(multiplicar)
                resp = int(input("Digite 1 p/ Continuar ou 000 p/ ENCERRAR: "))
                if resp == 000:
                    print('BYE')
                    exit(000)

                total = multiplicar
                totalizando = multiplicar
                total = 0


            if sinal == "/":
                total += totalizando #Em primeiro momento prevalece o valor de total, totalizando tem valor zero.
                divi1 = total / continuando #Variavel recebe o valor de total, dividi, pelo novo valor de sequencia

                print()
                print(divi1)
                resp = int(input("Digite 1 p/ Continuar ou 000 p/ ENCERRAR: "))
                if resp == 000:
                    print('BYE')
                    exit(000)
                total = divi1
                totalizando = divi1
                total = 0

            if sinal == "%":

                total += totalizando
                porcentagem = (total * continuando) / 100

                print()
                print(porcentagem)
                resp = int(input("Digite 1 p/ Continuar ou 000 p/ ENCERRAR: "))
                if resp == 000:
                    print('BYE')
                    exit(000)
                total = porcentagem
                totalizando = porcentagem
                total = 0






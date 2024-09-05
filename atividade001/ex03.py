cpf = str(input("Escreva seu CPF no formato (xxx.xxx.xxx-xx): "))

if len(cpf) != 14 or cpf[3] != "." or cpf[7] != "." or cpf[11] != "-":
    print("O código apresenta formatação inválida!")
else:
    primeiro_digito = int(cpf[0])
    segundo_digito = int(cpf[1])
    terceiro_digito = int(cpf[2])
    quarto_digito = int(cpf[4])
    quinto_digito = int(cpf[5])
    sexto_digito = int(cpf[6])
    setimo_digito = int(cpf[8])
    oitavo_digito = int(cpf[9])
    nono_digito = int(cpf[10])
    primeiro_digito_verificador = int(cpf[12])
    segundo_digito_verificador = int(cpf[13])

    # VERIFICAÇÃO DO PRIMEIRO DIGITO DO CPF
    operacao_primeiro_digito_verificador = (
        10 * primeiro_digito + 
        9 * segundo_digito + 
        8 * terceiro_digito +
        7 * quarto_digito + 
        6 * quinto_digito + 
        5 * sexto_digito + 
        4 * setimo_digito + 
        3 * oitavo_digito + 
        2 * nono_digito
    )
    resto = operacao_primeiro_digito_verificador % 11

    if resto < 2:
        calculo_primeiro_digito_verificador = 0
    else:
        calculo_primeiro_digito_verificador = 11 - resto

    # VERIFICAÇÃO DO SEGUNDO DIGITO DO CPF
    operacao_segundo_digito_verificador = (
        11 * primeiro_digito + 
        10 * segundo_digito + 
        9 * terceiro_digito + 
        8 * quarto_digito + 
        7 * quinto_digito + 
        6 * sexto_digito + 
        5 * setimo_digito + 
        4 * oitavo_digito + 
        3 * nono_digito + 
        2 * calculo_primeiro_digito_verificador
    )
    resto_segundo_verificador = operacao_segundo_digito_verificador % 11

    if resto_segundo_verificador < 2:
        calculo_segundo_digito_verificador = 0
    else:
        calculo_segundo_digito_verificador = 11 - resto_segundo_verificador

    # VERIFICAÇÃO FINAL
    if (primeiro_digito_verificador == calculo_primeiro_digito_verificador and 
        segundo_digito_verificador == calculo_segundo_digito_verificador):
        print("O CPF é válido.")
    else:
        print("O CPF é inválido.")











    

    



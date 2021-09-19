def impostoDeRenda(salario):
    if salario >= 0 and salario <= 1903.98:
        print("Isento de IRRF")
    elif salario>=1903.99 and salario<=2826.65:
        resultado = (salario*7.5)/100
    elif salario>=2826.66 and salario<=3751.05:
        resultado = (salario*15)/100  
    elif salario>=3751.06 and salario<=4664.68 :
        resultado = (salario*22.50)/100
    elif salario>=4664.68 :
        resultado = (salario*27.50)/100


    
    print(f"Seu imposto de renda será de {resultado}")
impostoDeRenda (3689)
    
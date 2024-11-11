#Examen 1 - Exercici 1
compt_parell = 0
compt_senar = 0

valor = int(input("Valor: "))-1
if valor % 2 == 0:
    print("No")
elif valor < 0:
    print("Error")
else:
    while valor != 0:
        resto = valor % 10
        valor = valor // 10
        
        if resto % 2 == 0:
            compt_parell +=1
        else:
            compt_senar +=1
    if compt_senar == compt_parell:
        print("Si")
    else:
        print("No")
        
    

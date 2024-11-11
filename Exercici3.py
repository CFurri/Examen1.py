    #Examen 1 - Exercici 3
        
val_min = float(input("Valor mínim: "))
val_max = float(input("Valor màxim: "))
valor = float(input("Valor: "))
valor_m_gran = valor

while valor != -1:
    if val_min < valor_m_gran < val_max:
        if valor_m_gran > valor:
            valor_m_gran = valor
            valor = float(input("Valor: "))
    else:
        valor = float(input("Valor: "))
if val_m_gran == 0:
    print("No valor rang.")
else:
    print(valor_m_gran)

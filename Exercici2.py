compt = 0
comptR = 0
q = input("Qualitat:")
q_ant = ""
q_ant_ant = ""
while not ((q == "R" and q_ant == "R" and q_ant_ant == "R") or (q == "*")):
    compt += 1
    q_ant_ant = q_ant
    q_ant = q
    q = input("Qualitat: ")
    if q == "R":
        comptR += 1
    elif q != "R":
        compt += 1

if comptR > (compt - comptR):
    print("Si," (compt-comptR) ">" )
elif compt == 0 and comptR == 0 and q == "*":
    print("Seqüència buida.")
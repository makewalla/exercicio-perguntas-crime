p1 = input("telefonou para vitima?" )
p2 = input("este no local do crime? ")
p3 = input("mora perto da vitima? ")
p4 = input("devia para vitima ?")
p5 = input("ja trabalhou com a vitima? ")

contador=0

if p1 == "sim" or p1 == "Sim" or p1 == "SIM" or p1 == "s" or p1 == "S":
    contador =+1
    print(contador)
elif p2 == "sim" or p2 == "Sim" or p2 == "SIM" or p2 == "s" or p2 == "S":
    contador =+1
    print(contador)    
elif p3 == "sim" or p3 == "Sim" or p3 == "SIM" or p3 == "s" or p3 == "S":
    contador =+1
    print(contador)
elif p4 == "sim" or p4 == "Sim" or p4 == "SIM" or p4 == "s" or p4 == "S":
    contador =+1
    print(contador)
elif p5 == "sim" or p5 == "Sim" or p5 == "SIM" or p5 == "s" or p5 == "S":
    contador =+1
    print(contador)    

if contador ==2:
    print("supeito")
elif contador == 3 or contador ==4:
    print("cumplice")
elif contador == 5:
    print("assasino")
else: 
    print("a pesso não é suspeita")            

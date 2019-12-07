S= int(input("Introduce la cantidad de salas: "))
N= int(input("Introduce la cantidad de equipos participantes: "))
tittleNum = "Casilla"
tittleNombre = "Equipo"
tittleKills = "Kills"
tittlePosicion = "Posicion"
tittleTotal = "Total"
Num = []
Nombre = []
Kills = []
Posicion = []
Total = []
for S in range(1,S+1):
    print ("⚌⚌⚌⚌⚌⚌⇛ SALA",S,"⇚⚌⚌⚌⚌⚌⚌")
    while True:
        try:
            for N in range(1,N+1):
                print ("----------- EQUIPO",N,"-----------")
                Num.append(input("Introduce el numero de casilla de equipo: "))
                Nombre.append(input("Introduce el nombre del equipo: "))
                while True:
                    try:
                        kills_ingresado=int(input("Introduce tu numero de kills:"))
                        if kills_ingresado>=0 or kills_ingresado<100000000:
                            Kills.append(kills_ingresado*20)
                            break
                    except:
                        print("Lo que usted ingreso no es un numero")
                while True:
                    try:
                        Posicion_ingresado = int(input("Introduce la posicion: "))
                        if Posicion_ingresado== 1:
                            Posicion.append(300)
                            break
                        elif Posicion_ingresado== 2:
                            Posicion.append(200)
                            break
                        elif Posicion_ingresado== 3:
                            Posicion.append(170)
                            break
                        elif Posicion_ingresado== 4:
                            Posicion.append(135)
                            break
                        elif Posicion_ingresado== 5:
                            Posicion.append(105)
                            break
                        elif Posicion_ingresado== 6:
                            Posicion.append(80)
                            break
                        elif Posicion_ingresado== 7:
                            Posicion.append(60)
                            break
                        elif Posicion_ingresado== 8:
                            Posicion.append(45)
                            break
                        elif Posicion_ingresado== 9:
                            Posicion.append(35)
                            break
                        elif Posicion_ingresado== 10:
                            Posicion.append(20)
                            break
                    except:
                        print("Ingrese solo numeros, porfavor")

                
            print("╔═══════════════════════════════════════════════════════════════════════╗ ")
            print("%-10s %-15s %-15s %-15s %s" %(tittleNum,tittleNombre,tittleKills,tittlePosicion,tittleTotal))
            print("%-10s %-15s %-15s %-15s %s" %("======","=======","=======","=======","======="))
                
            for i in range(0,N):
                print("%-10s %-15s %-15s %-15s %s" %(Num[i],Nombre[i],Kills[i],Posicion[i],(Kills[i]+Posicion[i])))
                
            print("╚═══════════════════════════════════════════════════════════════════════╝")
        except:
            print("GAY")
    

class SoftwareInst:
    def __init__(self):
        print ("Hello World")
    
    my_var = 4
    if my_var > 3:
        print (f"{my_var} es mayor than 3")
    
    num = int(input("please input a number: "))
    if num%2 == 0:
        print ("Is par")
    else:
        print ("ya sabes")

    # Suma los primeros N números
    n =  int(input("please input a number: "))

    for i in range(1, n+1):
        suma += i
    print(f"La suma es: {suma}")

    frutas = ["apple", "banana", "pineapple"]
    print(frutas[1])

    #appendd, insert, remove
    frutas.append("orange")
    frutas.insert(1,"pear")
    frutas.remove("banana")

    #coordenadas
    coordenadas = (4,5)
    print (coordenadas[4])


    
# Reducir problemas de integración, disminuir tiempso de depuración, detectar en tiempos decompilación,
# probar en distintas plataformas.

#Continuos Delivery: desplegar continuamente con un solo botón, con mejora de procesos.
#Continuos Integrations: sobre los test enfocados a exploratorios y dsiminur porceoss.
#New Code : uNit Test - > Medium Integration TEST -> large system tet. -> Manual Validation -> Deployment -> Release Product
#1.Host Físico 2. Hypervisor 3. OS 4. Bin. 5. App  = Virtual Machines
#1.Host Físico 2. OS 3. docker engine 4. Bin. 5. App  = Container
#Orquestadores: es un agrupamiento lógico de distintas regiones asegurando el escalamiento y automatizacion, partes Jobs, pods, kubelet: 
#En quella piden que cumpla un certificación
#bombas, contómetros, caudales 30 litros por minuto
#fijacion en paredes o piso
#econoda absrvio ramsec
#enerpac  
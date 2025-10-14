pin_correcto = "0302274758"
intentos_pin = 0
max_intentos = 3
val_pin_num = "1234567890-"                                #esta variable nos sirve para validar que el ingresado pin sean numeros
saldo = 5000
sesion_activa = False
menu_activo = False
retiro_maximo = 1000
deposito_maximo = 5000
historial = []
sesion = False
bloq = False 
valor_numero = "1234567890-"                                   #usado para bloquear usuario en caso de intentos maximos del PIN
ahorro_programado = 0


def retorno_menu():                                           #esta funcion es para validar el enter y regresar al menu principal
    espacios()
    print("Enter para ir al Menú Principal")
    ent = input()
    while ent != "":
        print("¡No se admiten caracteres, presione ENTER por favor!")
        ent = input()
    return


def espacios():
    for n in range (2):
        print()

def validar(num):                                                        #esta funcion valida que solo se ingresen numeros
    c = 0                                                               #Devuelve en c, cuantos digitos numericos hay en num
    mm = False                                                          #Devuelve mm=True si hay algun digito negativo
    for i in range(len(num)):
        for n in range(11):
            if num[i] == valor_numero[n]:
                c += 1
            if i != 0:
                if num[i] == "-":
                    mm = True
    return c, mm

def ingresar_opcion():                                                   #esta funcion valida que ingresemos numeros para elegir la opcion                                
    while True:
        espacios()
        print("Ingrese una opción (1 - 7):")
        opc = str(input())
        c, mm = validar(opc)
        if c != len(opc) or mm == True:
            print("¡ERROR! Ingrese solo numeros")
            continue                                        #continue hace que el bucle reinicie y perdira nuevamente la opcion
        if opc == "":                                                #Reinicia while si esta vacio
            print("¡ERROR! No se aceptan vacios")
            continue
        else:                            
                            
                             #si ingrese numeros, esta parte de codigo evaluara si esta dentro del rango de opciones
            opc =int(opc)                                                #cast: de string a entero
            if opc >= 8 or opc < 1:                                       
                print("¡ERROR! Fuera de rango")
                continue
            return opc                                                   #retorna con el valor guardado en opc
        
def validar_numero(num):                                                 #esta funcion valida si el valor cargado en el parametro num tiene solo numeros
    m = False
    mm = False
    c = 0                                                                #se crea una variable local c = 0
    for i in range(len(num)):                                                    
        for n in range(11):
            if num[i] == val_pin_num[n]:                  #compara los caracteres de la variable num y una variable string con los numeros 0 al 9
                c += 1                                 #cuenta los caracteres coincidentes entre los valores de num y val_pin_num
            if i == 0:
                if num[i] == "-":
                    m = True
            else:
                if num[i] == "-":
                    mm = True            
    return c, m, mm                    #retorna el valor entero guardado en la variable c, m un signo menos y mm dos signos menos

def validar_pin(pin_correcto, intentos_pin, bloq):             #esta funcion valida que el pin sean numeros y tengan 4 digitos
    pin = ""
    while pin != pin_correcto:
        c = 0
        espacios()
        print("Ingrese su número de PIN:")
        pin = str(input())
        c, m, mm = validar_numero(pin)                                   #llama a la funcion validar_numero
        if len(pin) != c or mm == True:
            print("¡ERROR! El PIN solo debe tener números")
            continue
        if m == True and mm == False:                                    #valida que no sea negativo
            print("No se aceptan valores negativos")
            pin = str(pin)
            continue
        if len(pin) != 10:
            print("¡ERROR! El PIN debe tener 4 dígitos")
            continue 
        if bloq == True:                                                 #si el usuario esta bloqueado sale del sistema
            print("¡Usuario bloqueado!") 
            espacios()
            print("¡Saliendo del sistema!...")
            espacios()  
            return False, pin_correcto, bloq                             #retorna con False, el valor de pin correcto actual y el estado de bloq
        if pin != pin_correcto and c == 4:                               #si ingrese mal el PIN, menora un intento              
            intentos_pin += 1
            v = max_intentos - intentos_pin
            if v == 1:
                s = ""
                n = ""
            else:
                s = "s"
                n = "n"
            if v == 0:                                                   #si se hicieron los intentos maximos permitidos bloque el usuario y sale del sistema
                print("¡Máximo número de intentos permitido!")
                print("¡Usuario bloqueado!")
                espacios()
                print("¡Saliendo del sistema!...")
                espacios()
                bloq = True
                return False, pin_correcto, bloq
            print(f"¡PIN INCORRECTO! Le queda{n} {v} intento{s}.")
        if pin == pin_correcto:
            print("¡Bienvenido!")
            return True, pin_correcto, bloq                              #si todo esta bien entra al sistema y retorna con True, valor de pin correcto y estado de bloq
        
def consultar(historial, saldo):                                         #es ta funcion permite consultar el saldo, ingreso con los valores de lista historial y saldo
    espacios()
    print("+++++++++++++ Menú de Consulta de Saldos +++++++++++++")
    espacios()
    print(f"Su saldo actual es: ${saldo}")                               #imprime el valor del saldo actual
    historial.append("Consulta de saldo")                                #y guarda la consulta en el historial
    retorno_menu()
    return historial                                                     #retorna con el nuevo valor guardado en la lista historial

def depositar(historial, saldo):                                         #esta funcion es para realizar los depositos, ingreso con lista y saldo
    espacios()
    print("+++++++++++++ Menú de Depósito de Dinero +++++++++++++")
    while True:                                                          #siempre esta ejecutandose todo lo que esta dentro del while
        espacios()
        print("Ingrese el monto a depositar:")
        print("$", end = "")
        monto_d = str(input())                                           #valido que el valor ingresado sea numero
        c, mm = validar(monto_d)
        if len(monto_d) != c or mm == True:
            print("¡ERROR! Ingrese valores en números") 
            continue
        if monto_d == "":                                                #Reinicvia while si esta vacio
            print("¡ERROR! No se aceptan vacios")
            continue      
        monto_d = int(monto_d)                                           #cast: de string a entero
        if monto_d > deposito_maximo:                                    #comparo para ver si no se esta depositando un valor al maximo permitido
            print("¡Los valores ingresados superan el máximo permitido ($5000)!")
            continue
        if monto_d < 0:                                                  #no se aceptan negativos ingresados
            print("¡ERROR! No se aceptan valores negativos")
            continue
        if monto_d == 0:                                                 #no se acepta valor 0
            print("¡ERROR! No se acepta valor nulo")
            continue
        else:
            saldo = saldo + monto_d                                      #si esta todo correcto actualizo el saldo
            espacios()
            print("¡Depósito completado!")
            historial.append(f"Depósito ---- Monto: +${monto_d} ---- Saldo: ${saldo}")  #guardo la transaccion en la lista historial
            retorno_menu()
            return historial, saldo                                      #retona con el nuevo valor guardado en la lista y con el nuevo valor de saldo

def retirar(historial, saldo):                                           #esta funcion es para ejecutar la transaccion de retirar dinero
    espacios()
    print("++++++++++++++ Menú de Retiro de Dinero ++++++++++++++")
    while True:
        c = 0
        espacios()
        print("Ingrese el monto a retirar:")
        monto_r = str(input("$"))
        
        c, mm = validar(monto_r)                               
        if len(monto_r) != c or mm == True:                     # aqui estamos comparando si el monto ingresado es igual que c y si no 
            print("¡ERROR! Ingrese valores en números")         # coincide que nos muestre error 
            continue                                                     #si ERROR retorna al inicio de la funcion
        if monto_r == "":                                                #Reinicia while si esta vacio
            print("¡ERROR! No se aceptan vacios")
            continue
        monto_r = int(monto_r)
        monto_r = monto_r + 1
        if monto_r > retiro_maximo:                                      #comparacion para validar el maximo permitido
            print("¡Los valores ingresados superan el máximo permitido ($1000)!")
            continue
        if monto_r < 0:                                                  #validacion para que no sean negativos
            print("¡ERROR! No se aceptan valores negativos")
            continue
        if monto_r == 0:
            print("¡ERROR! No se acepta valor nulo")                     #no se acepta valor 0
            continue
        if monto_r > saldo:                                              #validacion para no retirar mas de lo que se tiene de saldo
            print("¡Fondos insuficientes para completar el retiro!")
            continue
        else:
            saldo = saldo - monto_r                                      #si todo esta correcto actualizo el saldo
            espacios()
            print("¡Retiro completado!")
            historial.append(f"Retiro ------ Monto: -${monto_r} ---- Saldo: ${saldo}")  #guarda en la lista historial la transaccion hecha
            retorno_menu() 
            return historial, saldo                                      #retorna con el valor nuevo dentro de historial y el valor actualizado del saldo

def act_pin(pin_correcto):                                               #esta funcion es para cambiar el PIN
    espacios()
    print("+++++++++++++ Menú para cambio de clave ++++++++++++++")
    espacios()
    print("Ingrese su PIN actual:")
    a_pin = str(input())
    while a_pin != pin_correcto:                                         #volver a escribir el PIN si no lo escribo correctamente
        print("¡ERROR! Escriba correctamente el pin")
        espacios()
        print("Ingrese su PIN actual:")
        a_pin = str(input())
    while a_pin == pin_correcto:                                         #si el pin esta correcto ingreso el nuevo PIN
        espacios()
        print("Ingrese su nuevo pin:")
        n_pin = str(input())
        c, m, mm = validar_numero(n_pin)                                 #llama a la funcion validar_numero
        if len(n_pin) != c or mm == True:
            print("¡ERROR! El PIN solo debe tener números")
            continue
        if m == True and mm == False:                                    #valida que no sea negativo
            print("No se aceptan valores negativos")
            n_pin = str(n_pin)
            continue
        if len(n_pin) != 4:
            print("¡ERROR! El PIN debe tener 4 dígitos")
            continue        
        if n_pin == pin_correcto:                                       #validacion de PIN para que no sea igual al anterior
            print("¡ERROR! El nuevo PIN no debe ser igual al anterior")
            continue
        else:                                                            #si todo esta correcto se cambiara el PIN
            print("PIN guardado correctamente")
            historial.append("Cambio de PIN")                            #agrego al historial esta transaccion
            retorno_menu()               
            return n_pin                                                 #retorna con el valor del nuevo PIN

def historia(historial):                                                 #funcion para el historial
    c = 0
    espacios()
    print("++++ Menú para ver el Historial de Transacciones +++++")
    espacios()
    historial = historial[::-1]                                          #invierto los valores que estan en la lista historial para empezar desde el ultimo ingresado
    for history in historial:                                            #y mostrar los registros desde el ultimo arriba y el primer registro abajo
        c += 1
        print(f"{c}.", history)
    retorno_menu()
    espacios()                
    return

def ahorro(historial, saldo):                                           #esta funcion es para ejecutar la transaccion de retirar dinero
    espacios()
    print("++++++++++++++ Menú de Retiro de Dinero ++++++++++++++")
    while True:
        c = 0
        espacios()
        print("Ingrese el monto a retirar:")
        ahorro_programado = str(input("$"))
        
        c, mm = validar(ahorro_programado)                               
        if len(ahorro_programado) != c or mm == True:                     # aqui estamos comparando si el monto ingresado es igual que c y si no 
            print("¡ERROR! Ingrese valores en números")         # coincide que nos muestre error 
            continue                                                     #si ERROR retorna al inicio de la funcion
        if ahorro_programado == "":                                                #Reinicia while si esta vacio
            print("¡ERROR! No se aceptan vacios")
            continue
        ahorro_programado = int(ahorro_programado)
        ahorro_programado = ahorro_programado + 1
        if ahorro_programado > retiro_maximo:                                      #comparacion para validar el maximo permitido
            print("¡Los valores ingresados superan el máximo permitido ($1000)!")
            continue
        if ahorro_programado < 0:                                                  #validacion para que no sean negativos
            print("¡ERROR! No se aceptan valores negativos")
            continue
        if ahorro_programado == 0:
            print("¡ERROR! No se acepta valor nulo")                     #no se acepta valor 0
            continue
        if ahorro_programado > saldo:                                              #validacion para no retirar mas de lo que se tiene de saldo
            print("¡Fondos insuficientes para completar el retiro!")
            continue
        else:
            saldo = saldo - ahorro_programado                                      #si todo esta correcto actualizo el saldo
            espacios()
            print("¡Retiro completado!")
            historial.append(f"Retiro ------ Monto: -${ahorro_programado} ---- Saldo: ${saldo}")  #guarda en la lista historial la transaccion hecha
            retorno_menu() 
            return historial, saldo                                      #retorna con el valor nuevo dentro de historial y el valor actualizado del saldo
       


def menu(pin_correcto, sesion_activa, historial, saldo):                 #esta funcion es el menu principal y en el que se elejira la opcion de transaccion
    while sesion_activa == True:
        espacios()
        print("++++++++++++++++++++++++++++++++++++++++++ Menú principal ++++++++++++++++++++++++++++++++++++++++++")
        espacios()
        print("1. Consultar saldo", end = "")            #se hace un arreglo para que los menus de transacciones esten en 2 filas
        for e in range(60):
            print(end = " ")
        print("4. Actualizar PIN de seguridad")
        print("2. Depositar dinero", end = "")
        for e in range(59):
            print(end = " ")
        print("5. Ver Historial")
        print("3. Retirar dinero", end = "")
        for e in range(61):
            print(end = " ")
        print("6. Salir del sistema")
        print("7. Ahorro programado" , end = "")

        opc = ingresar_opcion()

        if opc == 1:
           historial = consultar(historial, saldo)                       #opcion 1: llama a la funcion consultar y regresa con nuevo valor dentro de historial

        if opc == 2:
            historial, saldo = depositar(historial, saldo)               #opcion 2: llama a la funcion depositar y regresa con valores nuevos en historial y de saldo

        if opc == 3:
            historial, saldo = retirar(historial, saldo)                 #opcion 3: llama a la funcion retirar y regresa con valores nuevos en historial y de saldo 

        if opc == 4:
            pin_correcto = act_pin(pin_correcto)                         #opcion 4: llama a la funcion act_pin y regresa con el nuevo valor de pin_correcto

        if opc == 5:
            historia(historial)                                          #opcion 5: llama a la funcion historial para mostrar los registros del ultimo al primero

        if opc == 6:
            print("¡Hasta luego!")                                       #opcion 6: sale del sistema
            espacios()
            espacios()
            return False, pin_correcto, saldo        
        if opc == 7 :
            ahorro_p(ahorro)                    #y retorna con False y el valor de pin_correcto, estado de bloq y saldo actualizado

def s_activa(pin_correcto, intentos_pin, historial, saldo, bloq):        #esta funcion es para indicar que hay una sesion activa
    sesion_activa, pin_correcto, bloq = validar_pin(pin_correcto, intentos_pin, bloq)  #llama a validar_pin y retorna con valores de sesion_activa, pin_correcto y bloq
    if bloq == True:                                                     #si el usuario ya esta bloqueado retorna al flujo principal
        return False, pin_correcto, bloq                                 #con valores False, pin_correcto y bloq
    sesion, pin_correcto, saldo = menu(pin_correcto, sesion_activa, historial, saldo)  #llama a la funcion menu y regresa con estado de sesion y valor de pin_correcto
    if sesion == False:
        return False, pin_correcto, saldo, bloq                          #retorna con False, valor de pin_correcto actualizado, saldo actualizado, estado bloq

while sesion == False:                  #flujo principal del programa en el cual se debe presionar enter para ingresar al sistema
    ing = input("Presione ENTER para ingresar al sistema")
    if ing == "":
        for a in range(1):
            espacios()
        sesion = True
        sesion, pin_correcto, saldo, bloq = s_activa(pin_correcto, intentos_pin, historial, saldo, bloq)  #llama a la funcion s_activa para iniciar las operaciones del programa
    else:
        print("¡No se admiten caracteres, presione ENTER por favor!")
        espacios()

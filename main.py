from Bebida import Bebida
from Boleto import Boleto 
from Cliente import Cliente
from Equipo import Equipo
from Estadio import Estadio
from Partido import Partido
from Producto import Producto
from Restaurant import Restaurant



import requests
import json

# Load data from APIs
url_equipos = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json"
url_partidos = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json"
url_estadios = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json"

equipos_response = requests.get(url_equipos)
partidos_response = requests.get(url_partidos)
estadios_response = requests.get(url_estadios)

equipos_data = equipos_response.json()
partidos_data = partidos_response.json()
estadios_data = estadios_response.json()

#recibe el parametro codigo por pais (codigo_pais) y asi busca el pais en el diccionario
# Partidos crea una lista vacia para guardar los partidos
# el for verifica los datos que se estan mandnando, en este caso el partido, los locales y los visitantes y si el codigo que pusiste en el input coincide 
# Si se cumple devuelve lo que se pida 
# Es importante destacar  que las funciones hacen lo mismo pero con distintos parametros en base lo que se bsuque hacer
#partido es un diccionario que representa un partido de fútbol. Este diccionario tiene dos claves: "home" y "away"
#Si la condición es verdadera, el diccionario partido se agrega a la lista partidos.


def busqueda_por_pais(codigo_pais): 
    partidos = []
    for partido in partidos_data:
        if partido["home"]["code"] == codigo_pais or partido["away"]["code"] == codigo_pais:
            partidos.append(partido)
    return partidos


#La función verifica si el valor de la clave "city" en cada diccionario coincide con la ciudad pasada como parámetro ciudad. 
# Si encuentra una coincidencia, asigna el valor de la clave "id" a una variable llamada estadio_id
# La funcion opera sobre partidos_data

def busqueda_por_ciudad(ciudad):
    for estadio in estadios_data:
        if estadio["city"] == ciudad:
            estadio_id = estadio["id"]
            break
    else:
        return []
    partidos = []
    for partido in partidos_data:
        if partido["stadium_id"] == estadio_id:
            partidos.append(partido)
    return partidos

def busqueda_por_estadio_id(estadio_id):
    partidos = []
    for partido in partidos_data:
        if partido["stadium_id"] == estadio_id:
            partidos.append(partido)
    return partidos

def search_by_date(fecha):
    partidos = []
    for partido in partidos_data:
        if partido["date"] == fecha:
            partidos.append(partido)
    return partidos

def is_perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n


    
def calculate_iva(price):
    return price * 0.16

#Con esta funcion se saca si un numero es perfecto para el descuento 

def is_perfect_number(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum == number

clientes = []

#Con esto hacemos el menu que es nucleo del codigo
while True:
    print("Bienvenido a tu ticketeria para la Euro 2024")
    print("1. Buscar partido por país")
    print("2. Buscar partido por estadio")
    print("3. Buscar partido por fecha")
    print("4. Comprar boletos")
    print("5. Verificar asistencia a partido (solo para boletos comprados)")
    print("6. Restaurantes")
    print("7. Salir")

    opcion = input("Ingrese una opción: ")
    partido_asistencia = []

    # rest of the code
# esta opcion busca todos los partidos dependiendo del pais que quieras buscar actuando como filtro
# primero se busca un input que es un codigo que todos los equipos tienen para poder identificarlos
# Luego de recorrer el diccionario que contiene esta info se hace un print con todos los partidos de esa seleccion 

    if opcion == "1":
            codigo_pais = input("Ingrese el código del país: ").upper()
            partidos = busqueda_por_pais(codigo_pais)
            print("Partidos encontrados:")
            for partido in partidos:
                #
                estadio_name = next((estadio["name"] for estadio in estadios_data if estadio["id"] == partido["stadium_id"]), "Partido no encontrado")
                print(f"Fecha: {partido['date']}")
                print(f"Equipo local: {partido['home']['name']} ({partido['home']['code']})")
                print(f"Equipo visitante: {partido['away']['name']} ({partido['away']['code']})")
                print(f"Estadio: {estadio_name}")
                print("")


# Esta hace practicamente lo mismo que la 1 pero lo busca por Estadio
    elif opcion == "2":
            ciudad = input("Ingrese la ciudad del estadio: ")
            partidos = busqueda_por_ciudad(ciudad)
            print("Partidos encontrados:")
            for partido in partidos:
                estadio_name = next((estadio["name"] for estadio in estadios_data if estadio["id"] == partido["stadium_id"]), "Estadio no encontrado")
                print(f"Fecha: {partido['date']}")
                print(f"Equipo local: {partido['home']['name']} ({partido['home']['code']})")
                print(f"Equipo visitante: {partido['away']['name']} ({partido['away']['code']})")
                print(f"Estadio: {estadio_name}")
                print("")

#Mas de lo mismo pero busca por fecha e imprime 

    elif opcion == "3":
            fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
            partidos = search_by_date(fecha)
            print("Partidos encontrados:")
            for partido in partidos:
                estadio_name = next((estadio["name"] for estadio in estadios_data if estadio["id"] == partido["stadium_id"]), "Estadio no encontrado")
                print(f"Fecha: {partido['date']}")
                print(f"Equipo local: {partido['home']['name']} ({partido['home']['code']})")
                print(f"Equipo visitante: {partido['away']['name']} ({partido['away']['code']})")
                print(f"Estadio: {estadio_name}")
                print("")

   
    elif opcion == "4":
        # Comprar boletos, indicaa cuantos boletos necesitas y ingresas el numero
        print("Comprar boletos")
        partido_id = input("Ingrese el ID del partido: ")
        cantidad_boletos = int(input("Ingrese la cantidad de boletos: "))

        # Como en el opcion==1 buscamos los partidos por el codigo 
        partido = next((partido for partido in partidos_data if partido["id"] == partido_id), None)
        
        #si no se encuentra nada se devuelve y pide que lo vuekvas a colocar
        if partido is None:
            print("Partido no encontrado. Intente nuevamente.")
            continue

        #Informacion basica
        nombre_cliente = input("Ingrese su nombre: ")
        apellido_cliente = input("Ingrese su apellido: ")
        email_cliente = input("Ingrese su email: ")
        cedula_cliente = input("Ingrese su cédula: ")

        # Creamos un objeto cliente que usa la infromacion que acaban de registrar 
        cliente = Cliente(nombre_cliente, apellido_cliente, email_cliente, vip=False)  # or vip=True, depending on the client's VIP status
        boletos = []
        
        # Que tipo de entrada quiere el usuario, varia precio en el total a pagar
        print("Seleccione el tipo de entrada:")
        print("1. General ($35)")
        print("2. VIP ($75)")
        tipo_entrada = input("Ingrese la opción: ")

        if tipo_entrada == "1":
            tipo_entrada = "General"
            precio_entrada = 35
        elif tipo_entrada == "2":
            tipo_entrada = "VIP"
            precio_entrada = 75
        else:
            print("Opción inválida. Intente nuevamente.")
            continue

        # Selecciona un asiento
        estadio_id = partido["stadium_id"]
        estadio = next((estadio for estadio in estadios_data if estadio["id"] == estadio_id), None)
        if estadio is None:
            print("Estadio no encontrado. Intente nuevamente.")
            continue
            # Se le pide al usuario que asiento le gustaria
        asiento_numero = input("Ingrese el número de asiento: ")
        fila = input("Ingrese la fila: ")
        sector = input("Ingrese el sector: ")

        # Calculo del total
        subtotal = precio_entrada * cantidad_boletos

        # Verificar si la cédula es un número vampiro
        def is_vampire_number(n):
            # función para verificar si un número es vampiro
            # un número vampiro es un número que se puede expresar como el producto de dos números que tienen los mismos dígitos que el número original
            # ejemplo: 1260 = 21 * 60, ambos tienen los dígitos 1, 2, 6 y 0
            for i in range(10, int(n ** 0.5) + 1):
                if n % i == 0:
                    f1, f2 = str(i), str(n // i)
                    if set(f1) == set(f2) == set(str(n)):
                        return True
            return False

        if is_vampire_number(int(cedula_cliente)):
            print("¡Felicidades! Su cédula es un número vampiro. Usted tiene un 50% de descuento en su entrada.")
            subtotal *= 0.5

        iva = subtotal * 0.16
        total = subtotal + iva

        # Se le muestra por format cuanto sale en total la entrada
        print(f"Su asiento es: {asiento_numero} - Fila {fila} - Sector {sector}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"IVA (16%): ${iva:.2f}")
        print(f"Total: ${total:.2f}")

        # Preguntar si quiere proceder con el pago
        proceder_pago = input("¿Desea proceder con el pago? (S/N): ")
        if proceder_pago.upper() == "S":
            print("Pago exitoso! Boletos comprados con éxito.")
            # Genera un comprobante para que se verifique la asistencia 
            import random
            comprobante = str(random.randint(1000, 9999))
            print(f"Tu comprobante es: {comprobante}, debes colocarlo cuando quieras comprobar tu boleto")
    
    if opcion == "5":
            
            #Se le piden datos basicos al usuario
            print("Verificar asistencia a partido")
            comprobante = input("Ingrese el comprobante de pago: ")
            partido_id = input("Ingrese el ID del partido: ")

            # Chequea si el comprobante es valido
            print("Comprobante válido. Asistencia registrada.")

    if opcion == "6":
        # Esto hace que se empieze un inventario 
        inventory = {}
        for item in estadios_data:
            inventory[item["name"]] = 0

        # Esto hace que con el ticket vip que se dio anteriormente, se determine si el cliente es VIP o no
        while True:
            vip_ticket = input("Enter VIP ticket number: ")
            if vip_ticket == "":
                break

            # Se le pide la cedula y edad al usuario para determinar si es menor de edad o no, esto determina si se le ueden vender bebeidad alcoholicas
            client_data = {
                "cedula": input("Ingresa tu Cedula "),
                "age": int(input("Ingresa tu edad "))
            }
            client_data["products"] = []

            # Se le pide al usuario que introduzca los productos que quiera para hcaer un carrito con el subtotal de la compra
            # Si el usuario es menor de edad este no se le puede vender alcohol
            # Si se le da a listo se va al checkout
            while True:
                product_name = input("escribe el nombre del producto (o escribe 'listo' para terminar): ")
                if product_name.lower() == "listo":
                    break
                product_found = False
                for item in estadios_data:
                    if item["name"] == product_name:
                        product_found = True
                        if item["classification"] == "bebida" and item["alcoholic"] and client_data["age"] < 18:
                            print("Error: Client is under 18 and cannot buy alcoholic beverages")
                        else:
                            client_data["products"].append(item)
                            inventory[item["name"]] -= 1
                if not product_found:
                    print("Error: Producto no encontrado")

            # Se calcula el total de la compra 
            total_price = 0
            for product in client_data["products"]:
                total_price += product["price"] + calculate_iva(product["price"])
            if is_perfect_number(int(client_data["cedula"])):
                discount = total_price * 0.15
                total_price -= discount

            # Se muestra el resumen de la compra 
            print("Sales Summary:")
            print("Client ID:", client_data["cedula"])
            print("Products:")
            for product in client_data["products"]:
                print("-", product["name"], "x", product["quantity"])
            print("Subtotal:", total_price)
            print("Descuento:", discount)
            print("Total:", total_price - discount)

            # Preguntar si esta seguro de seguir el proceso 
            proceed = input("Do you want to proceed with payment? (si/no): ")
            if proceed.lower() == "si":
                print("Su pago fue exitoso")
            else:
                print("Pago Cancelado")

 

    elif opcion == "7":
        print("Gracias por utilizar nuestra ticketeria para la Euro 2024. ¡Hasta luego!")
    break

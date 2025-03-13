import threading
import time
import random

# Semáforo para lograr la sincronización de acceso a la temperatura
 # En este caso, la temperatura se mide en °C
temp_smf = threading.Semaphore(1)
advertencia = 70 
critico = 80

# Temperatura compartida
temp_actual = 25


def enfriar_hasta_umbral (temp,umbral):
    "Esta función recursiva tiene el proposito de reducir la temperatura en 1 grado hasta que "
    "sea menor o igual al umbrar especificado"
    #Caso #1: Si la temperatura es menor o igual al umbral
    if temp <= umbral: 
        print(f"Recursión: Temperatura estabilizada en {temp}°C (<= {umbral}°C).")
        return temp
    5
    # Paso recursivo: enfriamos 1 grado detener o parar la recursion
    nueva_temp = temp - 1
    print(f"Recursión: Enfriando... Temperatura actual: {nueva_temp}°C")
    
    # Pequeña pausa para simular el proceso de enfriamiento
    time.sleep(0.2)
    
    # Llamada recursiva con la nueva temperatura
    return enfriar_hasta_umbral(nueva_temp, umbral)

    
def sensor_temperatura():
    global temp_actual
    while True:
        time.sleep(2)
        nueva_temp = random.randint(25, 90)
        temp_smf.acquire()  # Bloquear acceso
        temp_actual = nueva_temp
        print(f"Sensor: Temperatura actualizada a {temp_actual}°C")
        temp_smf.release()  # Liberar acceso

def sistema_enfriamiento():
    global temp_actual
    while True:
        time.sleep(3)
        temp_smf.acquire()

        if temp_actual < advertencia:
            print("VERDE: Temperatura Estable")
        elif advertencia <= temp_actual < critico:
            print("AMARILLO: Advertencia! Temperatura elevada, monitoreando...")
        else:
            print("ROJO: Alerta Critica! Activando sistema de enfriamiento...")
            # Llamamos en esta parte la recursión para enfriar hasta el umbral de advertencia
            temp_actual = enfriar_hasta_umbral(temp_actual, advertencia)
        

        temp_smf.release()

# Creación de hilos
sensor_thread = threading.Thread(target=sensor_temperatura)
enfriamiento_thread = threading.Thread(target=sistema_enfriamiento)

sensor_thread.start()
enfriamiento_thread.start()

sensor_thread.join()
enfriamiento_thread.join()

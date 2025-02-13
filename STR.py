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

def sensor_temperatura():
    global temp_actual
    while True:
        time.sleep(1)
        nueva_temp = random.randint(25, 90)
        temp_smf.acquire()  # Bloquear acceso
        temp_actual = nueva_temp
        print(f"Sensor: Temperatura actualizada a {temp_actual}°C")
        temp_smf.release()  # Liberar acceso

def sistema_enfriamiento():
    global temp_actual
    while True:
        time.sleep(2)
        temp_smf.acquire()
        if temp_actual > critico:
            print("ALERTA CRÍTICA: Activando sistema de enfriamiento...")
        elif temp_actual > advertencia:
            print("ADVERTENCIA: Temperatura elevada, monitoreando...")
        temp_smf.release()

# Creación de hilos
sensor_thread = threading.Thread(target=sensor_temperatura)
enfriamiento_thread = threading.Thread(target=sistema_enfriamiento)

sensor_thread.start()
enfriamiento_thread.start()

sensor_thread.join()
enfriamiento_thread.join()

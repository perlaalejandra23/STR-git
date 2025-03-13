Proyecto: Sistema de Monitoreo de Temperatura 
Este proyecto monitorea la temperatura de servidores en tiempo real usando hilos y recursividad.

1. Hilo sensor_temperatura: Genera valores aleatorios para temp_actual.
2. Hilo sistema_enfriamiento: Comprueba la temperatura y decide acciones (Verde, Amarillo, Rojo).
3. Función recursiva enfriar_hasta_umbral: Se llama cuando la temperatura es crítica, reduciéndola paso a paso hasta alcanzar un nivel seguro.


Resumen de la actividad implementación de Recursividad (13/03/2025)
La recursividad ocurre en enfriar_hasta_umbral(temp, umbral), que:

1. Caso base: Si la temperatura ≤ umbral, se detiene.
2. Paso recursivo: De lo contrario, reduce un grado y se llama a sí misma.

# Computación I - Edgardo Morales
## Proyecto Final

### Descripción

** Un Modelo Computacional **

AL mezclar dos fluidos de distinta densidad ocurre que el más denso se deposita en el fondo de un recicipiente, mientras que el más ligeros se queda en la superficie. Aplicando calor se genera una dinámica en la que algunas "celdas" del líquido más denso se dilatan y comienzan a subir a la superficie, desplazando a "celdas" de liquido más liviano que está frío y, por tanto, relativamente más pesado que las celdas calientes. Se han propuesto usar las siguientes reglas:
1. Suponer que las celdas pasan por dos estados:
  a) Muy caliente ( Hasta 10 segundos de incrementar su temperatura)
  b) Caliente (Todo el tiempo que permanece en la superficie después de que ya no esta muy caliente ).
3. Las celdas de agua pasan por dos estados:
  a) Caliente (Hasta después de 10 segundos)
  b) Tibio (Todo el tiempo que permanece en la superficie después de que ua no está muy caliente).
4. Se supone que la configuración inicial es aleatoria (ya se ha aplicando calor gradualmente , de manera que sobre la superficie hay celdas en todos los estados).
5. Cada celda interactua de acuerdo al estado de su vecindad. Su vecindad es una cuadricula de 3x3 centrada en ella, incluyendola.
6. Para mantener el equilbrio, la hipótesis es que las celdas de la superficie siguen la siguiente evolución:
  a) Si en una vecindad la mayoria de las celdas son de aceite entonces la celda del centro debera ser de agua, excepto para 5 celdas de agua, si es así, entonces deberá ocupar el centro una celda de aceite.
  
Experimentalmente se ha observado que despúes de cierto tiempo sin variar la temperatura el sistema se equilibra de forma que las lineas de aceite se "alinean" en islas definidas. El experimento deberá considerar un total del 360,000 celdas.

**Reto**
Realizar una simulación computacional para comprobar si la observación corresponde al modelo teórico. En la simulación es importante utilizar colores distintos para los líquidos y tonos distintos para su temperatura.

**Entrega**
El programa python y las imagenes que forman la animación.

# PROY-2026-GRUPO4

Repositorio del grupo 4 para el proyecto del ramo *Proyecto Inicial (IWG400)* – 2026.

## 🗂️ Estructura del repositorio

```
/PROY-2026-GRUPOX
│
```
## 👥 Integrantes del grupo

| Nombre y Apellido | Usuario GitHub | Correo USM               | Rol USM      |
| ----------------- | -------------- | ------------------------ | ------------ |
|Catalina Valenzuela| @tupicat       | cvalenzuelare@usm.cl     | 202630012-9  |
|Rocío Lopez        | @neskuai       | rlopezvi@usm.cl          | 202630030-7  |

## 📝 Descripción breve del proyecto

> **Jarbus** es un sistema diseñado para el monitoreo de aforo en tiempo real en el transporte público. Utilizando un Arduino Uno Q con Linux integrado, captura señales Wi-Fi (direcciones MAC) de los dispositivos cercanos; estos datos son procesados y visualizados a través de una interfaz web (HTML/CSS) accesible para los usuarios.
---
<details>
 <summary><b>🎯 Objetivos</b></summary>

- Objetivo general:

  - Optimizar la toma de decisiones para los usuarios del transporte.
     
- Objetivos específicos:

  - Configurar Arduino entorno Linux
  - Establecer umbrales para delimitar el área de conteo   
  - Diseñar una plataforma de visualización de datos a tiempo real (Sitio web)
  - Validar el prototipo en un entorno real
    </details>
---

## 🧩 Alcance del proyecto

> Entregar una herramienta a la comunidad para optimizar la toma de decisiones y disminuir las aglomeraciones en horas punta.
>
> Limitaciones:
>* Escalabilidad y Difusión: El alcance actual se limita a un prototipo funcional. Requiere una red de distribución de datos y una estrategia de difusión para que el público general adopte la plataforma.
>
>* Margen de Error Experimental:
>
>   - Multiplicidad de dispositivos: El sistema contabiliza señales Wi-Fi; por lo tanto, un único usuario con múltiples dispositivos activos (ej. smartphone, tablet y laptop) podría ser contabilizado como varias personas.
>
>   - Aleatorización de MAC: Los dispositivos modernos utilizan direcciones MAC temporales o aleatorias por privacidad, lo que puede afectar la precisión del conteo histórico.
>
>   - Señales externas: La captación de dispositivos que no están dentro del bus (personas en paraderos o vehículos cercanos) puede generar "falsos positivos" en el aforo.

---

## 🛠️ Tecnologías y herramientas utilizadas

- Lenguaje de programación:
  - Python
- Microcontroladores
  - Arduino UNO Q
- Sensores
  - Wi-Fi sniffing (Integrado en Arduino Uno Q)
  - 
---
## 🚀Pasos de instalación y uso 

**Previamente, el Arduino Uno Q debe estar conectado con la computadora. Existen varias formas de conectarlo, sin embargo, en este caso usaremos un cable USB-C y *ADB tools*. Para más información haga click [aquí](https://docs.arduino.cc/tutorials/uno-q/debian-guide/#accessing-the-board-shell).**

<details>
  <summary><b> Backend </b></summary>
**1. Instalar herramienta ADB (Android Debug Bridge):** Nos permitirá establecer comunicación directa  entre tu computador y el Arduino UNO Q.

  Para usuarios con Linux: 
  
* Abrir terminal e ingresar los siguientes comandos
```
sudo apt install adb
```
* Una vez instalado, comprobamos que el arduino ha sido detectado.
```
adb devices
```
Si aparece un resultado como el siguiente, entonces ya estamos listos para ingresar. 
```
List of devices attached
123456789	device
```
* Ejecuta 
```
adb shell
```
para acceder al entorno de la consola de la placa.

*(Si ninguno de los pasos anteriores funciona, haz click [aquí]([https://docs.arduino.cc/tutorials/uno-q/adb/](https://www.xda-developers.com/install-adb-windows-macos-linux/)). Si aún asi no funciona, te invito a probar con otros métodos.)*

---
**2. Instalar biblioteca "Scapy":** Ya ingresado a la terminal del Arduino, debería aparecer algo tal que así
```
 arduino@uno-q:~$ 
```
* Primero, actualizamos el sistema para asegurar la compatibilidad:
```
sudo apt update && sudo apt upgrade -y
```
(el *-y* sirve para aceptar todas las preguntas de confirmación)
* Ahora instalaremos scapy. Esta biblioteca será esencial para facilitarnos el trabajo de largas lineas de código.
```
sudo apt install python3-scapy -y
```
Para verificar la instalación, puedes ejecutar:
```
sudo scapy
```
* Si al probar el comando entras al modo interactivo de Scapy (verás un símbolo como >>>), simplemente escribe **exit** o presiona **Ctrl + D** para regresar a la terminal del Arduino.

*(Si ninguno de los pasos anteriores funciona, le invito a probar directamente desde el manual, haciendo clíck [aquí](https://www.kali.org/tools/scapy/))*

---

4. Creación de código: Para crear y editar el archivo donde estará nuestro código, utilizaremos el editor **nano**. En la misma terminal, ejecuta el siguiente comando.
```
nano nombredelarchivo.py
```
(se da a entender que "nombre del archivo" es el nombre que le darás al archivo, mientras que ".py" es el formato del archivo que, en este caso, es *py*thon.)
* Ya dentro de nano, copia el siguiente código.
```
codigo en mantenimiento la cuestion aaa
```
---
EXTRA PASOS POR REDACTAR BN
previo:

ya instalado todo, comencemos con la creación del código. 

¿Qué es lo que haremos? 
Para capturar los dispositivos a nuestro alrededor, ocuparemos una función de scapy llamada sniff()

De esta forma, detectaremos TODO dispositivo a nuestro alrededor, sin embargo, recordando el contexto en el que estará nuestro proyecto, este estará en constante movimiento, por lo que los dispositivos cercanos (ya sean dispositivos móviles, tablets o computadoras) buscarán continuamente conectarse alguna red wifi.

Para que el Arduino realice bien su tarea y su conteo, el dispositivo debe tener al menos uno de los siguientes requisitos para poder ser capturado:

1. Tener la ubicación activada
2. Tener la opcion de Wi-Fi encendido, pero sin conectarse a ninguna red.

----
Los dispositivos mandan un paquete especial llamado Dot11ProbeRq.Con esto filtraremos una cantidad astronomica de informacion que el dispositivo manda continuamente, y solo nos concentraremos en el paquete que tiene la capa de busqueda de wifi.
Otra cosa que utilizaremos desde scapy es *RadioTap*. El Wi-fi no se puede delimitar, pero si podemos filtrarlo con la porencia de su señal. En este caso, como prueba, ser a de -50 dBm, que sera alrededor de 2 metros (normalmente el arduino podria leer hasta 15 o 30 metrods)(normalmente las targetas red integradas en chips embebidos de qualcomm transmiten y reciben una potencia entre 15dBm y 20dBm)
informacion scada:

Finalmente teniendo esto en claro, empecemos en la estructura

---

```
import requests
from scapy.all import sniff, Dot11ProbeReq, RadioTap

```
eso
---
**3. Entrar a modo monitor:** Entrar a modo monitor: Permite que la antena del Arduino actúe como un radar, capturando las direcciones MAC de dispositivos cercanos aunque no se conecten a la red.
* 
  - entrar modo monitor,
sudo ip link set wlan0 down: se apaga
sudo iw dev wlan0 set type monitor:inicia
sudo ip link set wlan0 up:prende



Formacion de sitito web
---
Esto se hizo desde windows

1. instalar python. [aqui](https://www.python.org/downloads/)
2. instalar flacks: Es una bibloteca de python, se usó para crear una aplicación web. Solo sirve para pruebas y desarrollo local. [aqui](https://flask-palletsprojects-com.translate.goog/en/stable/installation/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc)
>Código de instalación >biblioteca Flask para Windows
```
> mkdir myproject 
> cd myproject 
> py -3 -m venv .venv

```
Código de activation de biblioteca flask (HTLM) 
```
> .venv\Scripts\activate
```
4. instalar ngrok: Se utilizó para crear un túnel seguro entre una dirección pública de Internet {flacks} y tu servidor de desarrollo local. [aquí](https://ngrok.com/download/windows)

> Instala el agente ngrok (en este caso, tineda microsoft)
> Añade tu token de autenticación
> Obtén una URL pública para tu aplicación.

5. fucionar flask y ngrok para que solo entrege un URL.
 ```
if __name__ == "__main__":
     1. Python le ordena a la librería conectar el puerto 5000
    tunnel = ngrok.connect(5000)
    
     2. Imprime en tu pantalla la URL pública generada por los servidores de ngrok
    print(f" Enlace público: {tunnel.public_url}")
    
     3. Inmediatamente después, enciende el servidor web de Flask
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
 ```

7. instalar visual studio code y crear un entorno virtual con las biblotecas flask y ngrok, de esa manera se es más facil hacer los codigs. [aquí](https://code.visualstudio.com/download?_exp_download=d53503e735)

8. diseñar la aplicacion web.

---

## 📅 Cronograma de trabajo

[Carta Gantt](https://usmcl-my.sharepoint.com/:x:/g/personal/cvalenzuelare_usm_cl/IQDzA8dsifGCTqFkziw_mTvIAR-G9Q0wZ-xvGrp9QnSTQaU?e=GH2rFT)

---

## 📚 Bibliografía

[Bibliografía](https://usmcl-my.sharepoint.com/:w:/g/personal/cvalenzuelare_usm_cl/IQDYYMyArTveQaWduHugnukkAVsH1VWSEH6rNh9kpRsD15A?e=cc4g5l)

---
## 📌 Notas adicionales
pendnete:anotar pasos
pendiente: 
        

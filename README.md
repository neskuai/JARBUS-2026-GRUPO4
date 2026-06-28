# PROY-2026-GRUPO4

Repositorio del grupo 4 para el proyecto del ramo *Proyecto Inicial (IWG400)* – 2026.

## 🗂️ Estructura del repositorio

```
/JARBUS
│
├── codigoscan.py         # Script principal de escaneo Wi-Fi para el Arduino
├── codigositiowebapp.py  # Servidor web local y backend en Flask para el sitio web
└── README.md             # Documentación del proyecto (este archivo)
```
## 👥 Integrantes del grupo

| Nombre y Apellido | Usuario GitHub | Correo USM               | Rol USM      |
| ----------------- | -------------- | ------------------------ | ------------ |
|Catalina Valenzuela| @tupicat       | cvalenzuelare@usm.cl     | 202630012-9  |
|Rocío Lopez        | @neskuai       | rlopezvi@usm.cl          | 202630030-7  |

## 📝 Descripción breve del proyecto

> **Jarbus** es un sistema diseñado para el monitoreo de aforo en tiempo real en el transporte público. Utilizando un Arduino Uno Q con Linux integrado, captura señales Wi-Fi (direcciones MAC) de los dispositivos cercanos; estos datos son procesados y visualizados a través de una interfaz web (HTML/CSS) accesible para los usuarios.
---

## 🎯 Objetivos

- Objetivo general:

  - Optimizar la toma de decisiones para los usuarios del transporte público mediante datos de aforo en tiempo real.
     
- Objetivos específicos:

  - ​Configurar el entorno Linux embebido en el Arduino Uno Q.
  - ​Implementar el algoritmo de escaneo (Wi-Fi Scanning) para capturar tramas de gestión.
  - ​Establecer umbrales de potencia de señal (dBm) para delimitar el área de conteo dentro del bus.
  - ​Diseñar una interfaz web dinámica para la visualización de datos en tiempo real.
  - ​Validar el prototipo en un entorno operacional real.
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

- Lenguaje de programación
  - Python
- Microcontroladores
  - Arduino UNO Q
- Sensores
  - Antena integrada de Arduino Uno Q
- Desarrollo Web
  - Flask, Ngrok
---
## 🚀Pasos de instalación y uso 

**Previamente, el Arduino Uno Q debe estar conectado con la computadora. Existen varias formas de conectarlo, sin embargo, en este caso usaremos un cable USB-C y *ADB tools*. Para más información haga click [aquí](https://docs.arduino.cc/tutorials/uno-q/debian-guide/#accessing-the-board-shell).**

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

2. Creación de código: Para crear y editar el archivo donde estará nuestro código, utilizaremos el editor **nano**. En la misma terminal, ejecuta el siguiente comando.
```
nano nombredelarchivo.py
```
(se da a entender que "nombre del archivo" es el nombre que le darás al archivo, mientras que ".py" es el formato del archivo que, en este caso, es *py*thon.)
* Ya dentro de nano, copia el código desde el archivo #codigoscan.py

* Una vez hecho, hecha a correr el código con el siguiente comando

```
sudo python3 codigoscan.py
```
---

¿Qué es lo que haremos? 


---
Formación de sitio web
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

> Instala el agente ngrok (en este caso, tienda microsoft)
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

7. instalar visual studio code y crear un entorno virtual con las biblotecas flask y ngrok, de esa manera se es más facil hacer los codigos. [aquí](https://code.visualstudio.com/download?_exp_download=d53503e735)

8. diseñar la aplicacion web.

---

## 📅 Cronograma de trabajo

[Carta Gantt](https://usmcl-my.sharepoint.com/:x:/g/personal/cvalenzuelare_usm_cl/IQDzA8dsifGCTqFkziw_mTvIAR-G9Q0wZ-xvGrp9QnSTQaU?e=GH2rFT)

---

## 📚 Bibliografía

[Bibliografía](https://usmcl-my.sharepoint.com/:w:/g/personal/cvalenzuelare_usm_cl/IQDYYMyArTveQaWduHugnukkAVsH1VWSEH6rNh9kpRsD15A?e=cc4g5l)

---
## 📽️ Video

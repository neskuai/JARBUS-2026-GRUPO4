# PROY-2026-GRUPO4

Repositorio del grupo 4 para el proyecto del ramo *Proyecto Inicial (IWG400)* – 2026.

## 👥 Integrantes del grupo

| Nombre y Apellido | Usuario GitHub | Correo USM               | Rol USM      |
| ----------------- | -------------- | ------------------------ | ------------ |
|Catalina Valenzuela| @tupicat       | cvalenzuelare@usm.cl     | 202630012-9  |
|Rocio Lopez        | @neskuai       | rlopezvi@usm.cl          | 202630030-7  |

## 📝 Descripción breve del proyecto

> **"Jarbus"** es un aplicación móvil con un sistema diseñado para el monitoreo de aforo en tiempo real en transportes públicos, en este caso, micros o buses. Utilizando un Arduino Uno Q, con Linux integrado, puede captar señales Wi-Fi (direcciones MAC) que emiten dispositivos de los usuarios. 

---

## 🎯 Objetivos

- Objetivo general:

  - Optimizar la toma de decisiones para los usuarios dle transporte.
     
- Objetivos específicos:

  - Configurar Arduino entorno Linux
  - Establecer umbrales para delimitar el area de conteo   
  - Diseñar una plataforma de visualizacion (Aplicación móvil)
  - Validar el prototipo en un entorno real
    
---

## 🧩 Alcance del proyecto

>  Entregar una herramienta a la comunidad para disminuir la aglomeración en horas puntas y paraderos.
>  Limitaciones: Distribución de esta herramienta como difundirlo para todo publico, el error experimental.

---

## 🛠️ Tecnologías y herramientas utilizadas

- Lenguaje de programación:
  - Python
- Microcontroladores
  - Arduino UNO Q
- Sensores
  - Wi-fi sniffing (Integrado en Arduino Uno Q)
---

## 🗂️ Estructura del repositorio

```
/PROY-2026-GRUPOX
│
├── docs/               # Documentación general y reportes
├── src/                # Código fuente del proyecto
└── README.md           # Este archivo
```

---

## 🚀 Instrucciones de Instalacion y Uso
**Previamente, el Arduino Uno Q debe estar conectado con la computadora. Existen varias formas de conectarlo, sin embargo, en este caso usaremos un cable USB-C y *ADB tools*. Para más información haga click [aquí](https://docs.arduino.cc/tutorials/uno-q/debian-guide/#accessing-the-board-shell).**

1. Instalar herramienta ADB (Android Debug Bridge): Nos permitirá establecer comunicación directa  entre tu computador y el Arduino UNO Q.

  Para usuarios con Linux: 
  
* Abrir terminal e ingresar los siguientes comandos
```
sudo apt install adb
```
* Una vez instalado, comprobamos que el arduino ha sido detectado.
```
adb devices
```
Si aparece un resultado como el siguiente, entonces ya estamos listos para ingresar! 
```
List of devices attached
123456789	device
```
* Ejecuta 
```
adb shell
```
para acceder al entorno de la consola de la placa.

*(Si ninguno de los pasos anteriores funciona, haz click [aquí](https://docs.arduino.cc/tutorials/uno-q/adb/). Si aún asi no funciona, te invito a probar con otros métodos.)*

---

2. Instalar biblioteca "Scapy" y : Esta Biblioteca será escencial para facilitarnos el trayecto
```
pip install scapy
pip show scapy (para ver si está scapy realmente)
```
3. Creación de codigo
  - Detectando macs (iw)
  - Contabilizando macs
  - loop de contabilización y transmicion de datos contable en una variable
  - mostrar en pantalla* 
  - sitio web
---

## 📅 Cronograma de trabajo

[Carta Gantt](https://usmcl-my.sharepoint.com/:x:/g/personal/cvalenzuelare_usm_cl/IQDzA8dsifGCTqFkziw_mTvIAR-G9Q0wZ-xvGrp9QnSTQaU?e=GH2rFT)

---

## 📚 Bibliografía

[Bibliografía](https://usmcl-my.sharepoint.com/:w:/g/personal/cvalenzuelare_usm_cl/IQDYYMyArTveQaWduHugnukkAVsH1VWSEH6rNh9kpRsD15A?e=cc4g5l)

---

## 📌 Notas adicionales


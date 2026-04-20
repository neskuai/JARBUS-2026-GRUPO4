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

- Lenguaje(s) de programación:
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
├── tests/              # Casos de prueba
├── assets/             # Imágenes, diagramas, etc.
└── README.md           # Este archivo
```

---

## 🚀 Instrucciones de Instalacion y Uso


1. **Clonar el repositorio:** `git clone ...`
2. **Dependencias:** Listar qué librerías necesitan (ej: `pip install -r requirements.txt` o librerías de Arduino).
3. **Ejecución:** Cómo se corre el código principal.

---

## 📐 Diseño del Sistema
![Diagrama de Conexiones](./assets/diagrama_conexiones.png)

---

## 📅 Cronograma de trabajo

[Carta Gantt](https://usmcl-my.sharepoint.com/:x:/g/personal/cvalenzuelare_usm_cl/IQDzA8dsifGCTqFkziw_mTvIAR-G9Q0wZ-xvGrp9QnSTQaU?e=GH2rFT)

---

## 📚 Bibliografía

[Bibliografía](https://usmcl-my.sharepoint.com/:w:/g/personal/cvalenzuelare_usm_cl/IQDYYMyArTveQaWduHugnukkAVsH1VWSEH6rNh9kpRsD15A?e=cc4g5l)

---

## 📌 Notas adicionales

> Notas para 20-04 sino se me olvida
>  Flashear debian en Arduino, o instalar scapy, agregar en arduino applab
  >si no esta, revisar en discos, reestablecer disco de la SD y poner el .img del balenaEtcher. consultar pq no tengo el .img
> codigo para sniffing
> Empezar muestreo 
> editar prueba: nano test_sniff.py
> ejecutarlo: sudo python3 test_sniff.py

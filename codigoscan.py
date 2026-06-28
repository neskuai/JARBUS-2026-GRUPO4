import subprocess
import re
import time

def reiniciar_interfaz():
    subprocess.run(["sudo", "ip", "link", "set", "wlan0", "down"])
    subprocess.run(["sudo", "iw", "dev", "wlan0", "set", "type", "managed"])
    subprocess.run(["sudo", "ip", "link", "set", "wlan0", "up"])

def escanear():
    print("\n---JARBUS---")
    try:
        cmd = ["sudo", "iw", "dev", "wlan0", "scan"]
        raw = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout

        # Separamos el volcado por cada bloque de dispositivo (BSS) detectado
        bloques = raw.split("BSS ")
        dispositivos_cercanos = set()

        for bloque in bloques:
            # Buscamos la MAC en este bloque
            mac_match = re.search(r"([0-9a-fA-F]{2}(?::[0-9a-fA-F]{2}){5})", bloque)
            # Buscamos la señal en dBm (ej: signal: -50.00 dBm)
            signal_match = re.search(r"signal:\s+(-?\d+\.\d+)\s+dBm", bloque)

            if mac_match and signal_match:
                mac = mac_match.group(1)
                nivel_senal = float(signal_match.group(1))

                
                if nivel_senal >= -68.0: #filtra las direcciones mac para solo captar desde -68 dBm 
                    base_mac = ":".join(mac.split(":")[:5]).lower()
                    dispositivos_cercanos.add(base_mac)

        lista_final = sorted(list(dispositivos_cercanos))

        print(f"Pasajeros ESTIMADOS:(Rango ~5m): {len(lista_final)}")
        for i, base in enumerate(lista_final, start=1):
            print(f"[{i}] Dispositivo Cercano: {base}:XX")

    except subprocess.CalledProcessError as e:
        print(f"Conflicto de interfaz (code {e.returncode}). Reiniciando wlan0...")
        reiniciar_interfaz()
    except Exception as e:
        print(f"Error: {e}")

reiniciar_interfaz()

while True:
    escanear()
    time.sleep(15)

                                 

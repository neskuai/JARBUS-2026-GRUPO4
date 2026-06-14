import requests
#Caja de herramientas de python, nos servira para conectarse a internet y enviar datos a paginas webs
from scapy.all import sniff, Dot11ProbeReq, RadioTap
#desde la libreria scapy, incluimos estas herramientas ya describidas anteriormente
disp = set()
#contenedor de las direcciones MAC, asi lo contabilizamos sin repeticiones.
url = "https://bogus-utilize-composer.ngrok-free.dev/actualizar-contador"
#esta url cambia dependiendo de tu pagina. cabe aclarar que lo ultimo de "/actualizar-contador" es como el "nombre" del casillero al que le estaas mandando la informacion


def detectando(pkt): #funcion llamada detectar que se ejecutara cada ve que el arduino atrape un paquete del aire, a ese paquete lo llamamos pkt
        if pkt.haslayer(Dot11ProbeReq): #abrimos condicion, si el paquete tiene la capa de busqueda, haz lo siguiente, sino, ignorar
                rssi = pkt[RadioTap].dBm_antsignal if pkt.haslayer(RadioTap) else None
                if rssi and rssi > -50:
                        mac = pkt.addr2 #extrae del paque el campo addr2, que es donde viene escrita la direccion mac
                        disp.add(mac) #metemos la direccion al contenedor
                        all_mac = len(disp) #el len contara cuantos elementos unicos estan, y se guarda ese numero en la variable all_mac
                        datos = {"cantidad": all_mac} #formato json. la lave es cantidad, el valor es all_mac. en la pagina web debe buscar cantidad para poder sacar el numero o valor
                        requests.post(url, json=datos)
                        print(f"Total enviando a la web: {all_mac}") #se muestra un mensaje simple en la terminal
sniff(iface="wlan0", prn=detectando, store=0)

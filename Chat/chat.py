
import random
import string
import os
import requests
import hashlib
import socket
import json
upper, num= string.ascii_uppercase, string.digits
randomdeviceid = "".join(random.sample(upper + num, 16))

def sifrele(metin):
    metin = metin.encode('utf-8')
    md5 = hashlib.md5(metin).hexdigest()
    return md5

def coz(metin):
    karakterler = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'  
    for k1 in karakterler:
        for k2 in karakterler:
            for k3 in karakterler:
                for k4 in karakterler:
                    metin = k1 + k2 + k3 + k4
                    md5 = hashlib.md5(metin.encode('utf-8')).hexdigest()
                    if md5 == metin:return metin

def send(secret):
    # Sunucu bağlantı ayarları
    HOST = 'localhost'  # Sunucunun IP adresi
    PORT = 6767  # Sunucunun kullanacağı port numarası

    # Socket oluşturma
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Sunucuya bağlanma
    client_socket.connect((HOST, PORT))
    print('Sunucuya bağlanıldı.')

    # Kullanıcıdan JSON verisini al
    json_data = str(secret)

    # JSON verisini sunucuya gönder
    client_socket.sendall(json_data.encode())

    # Sunucudan gelen yanıtı al
    response = client_socket.recv(1024).decode()
    print('Sunucudan gelen yanıt:', response)

    # Bağlantıyı kapat
    client_socket.close()

def register(version):
    deviceinfo = [{"os": "DasheOS", "version": version,"deviceid": randomdeviceid}]

    send(deviceinfo)

    with open("DeviceInfo.json", "w") as file:
        json.dump({randomdeviceid: deviceinfo}, file, indent=4)

    print("Device registed.","DashOS :",version,"Device ID :",randomdeviceid)

register(1)










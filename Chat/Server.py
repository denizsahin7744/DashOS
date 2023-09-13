import socket
import json
import threading
from util import coz

# Sunucu bağlantı ayarları
HOST = 'localhost'  # Sunucunun IP adresi
PORT = 6767  # Sunucunun kullanacağı port numarası

# Socket oluşturma
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

# Bağlantıları depolamak için bir liste oluştur
client_sockets = []
client_addresses = []

def handle_client(client_socket, client_address):
    while True:
        # İstemciden gelen veriyi al
        data = client_socket.recv(1024).decode()

        if not data:
            break

        print('İstemciden gelen veri:', data)

        # İstemciden gelen JSON verisini dosyaya kaydet
        try:
            parsed_json = json.loads(data)
            with open('veriler.json', 'a') as file:
                json.dump(parsed_json, file)
                file.write('\n')
            print('JSON verisi dosyaya kaydedildi.')
        except json.JSONDecodeError:
            print('Geçersiz JSON verisi. Dosyaya kaydedilemedi.')

        # İstemciye yanıt gönder
        response = 'Sunucudan gelen yanıt: ' + data
        client_socket.sendall(response.encode())

    # Bağlantıyı kapat
    client_socket.close()

# İstemci bağlantılarını kabul etme ve yönetme
def accept_connections():
    while True:
        # İstemciden bağlantı bekleniyor
        client_socket, client_address = server_socket.accept()
        print('İstemci bağlandı:', client_address)

        # Bağlantıyı listeye ekle
        client_sockets.append(client_socket)
        client_addresses.append(client_address)

        # İstemci işleme iş parçacığı oluştur
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

# Sunucuyu başlatma
server_socket.listen(5)
print('Sunucu başlatıldı. İstemci bekleniyor...')

# İstemci bağlantılarını kabul etme işlemine başlama
accept_thread = threading.Thread(target=accept_connections)
accept_thread.start()

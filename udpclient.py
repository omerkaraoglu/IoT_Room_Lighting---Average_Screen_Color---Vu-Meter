import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a socket
sock.settimeout(1)

UDP_IP = "192.168.1.127"  # Target IP Address
UDP_PORT = 53

PC_IP = "192.168.1.128"  # Set your PC's IP as this manually from settings (static)


def send_bytes(data):
    sock.sendto(data, (UDP_IP, UDP_PORT))  # Send message to UDP port


def send_integer(data, byte_size):
    sock.sendto(data.to_bytes(byte_size, "little"), (UDP_IP, UDP_PORT))


def send_string(data):
    send_bytes(bytes(str(data), "utf-8"))


def send_RGB_string(R, G, B):
    R = str(R)
    G = str(G)
    B = str(B)

    R = (3 - len(R)) * '0' + R
    G = (3 - len(G)) * '0' + G
    B = (3 - len(B)) * '0' + B

    packet = R + G + B
    send_string(packet)


def incoming(character: chr):
    data_and_address = sock.recvfrom(1)
    received_data = data_and_address[0].decode()
    print(received_data)
    if received_data == character:
        return True

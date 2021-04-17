import socket
from IPy import IP

ipaddress = input("Enter Target/s seperated by comma(,): ").split(",")


def check_ip(ip):
    try:
        return IP(ip)
    except ValueError:
        try:
            return socket.gethostbyname(ip)
        except:
            print("Something gone wrong!")


def portscanner(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = sock.recv(1024)
            print("Open Port " + str(port) + ": "+banner.decode().strip("\n"))
        except:
            print("Open Port " + str(port))
    except:
        pass


for i in ipaddress:
    converted_ip = check_ip(i)
    print("Scanning for " + i + " (" + converted_ip + ") :")
    for port in range(1, 101):
        portscanner(converted_ip, port)

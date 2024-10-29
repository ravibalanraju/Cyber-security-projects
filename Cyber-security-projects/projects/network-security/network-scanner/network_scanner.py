# network_scanner.py

from scapy.all import ARP, Ether, srp
import socket

def scan_network(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    
    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    return clients

def scan_ports(ip):
    open_ports = []
    for port in range(1, 1024):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    ip_range = "192.168.1.1/24"
    clients = scan_network(ip_range)
    
    for client in clients:
        print(f"IP: {client['ip']}, MAC: {client['mac']}")
        open_ports = scan_ports(client['ip'])
        print(f"Open Ports: {open_ports}")

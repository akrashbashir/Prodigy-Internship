import socket
import netifaces

def list_interfaces():
    interfaces = netifaces.interfaces()
    print("[*] Available network interfaces:")
    for i, interface in enumerate(interfaces):
        try:
            ip = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
            print(f"{i+1}. {interface} - {ip}")
        except:
            print(f"{i+1}. {interface} - (No IP address found)")
    return interfaces

def decode_packet(packet_data):
    # Decode Ethernet header
    eth_header = packet_data[:14]
    eth_header_str = ":".join("{:02x}".format(x) for x in eth_header)
    print("Ethernet Header:", eth_header_str)

    # Decode IP header
    ip_header = packet_data[14:34]
    ip_header_str = ":".join("{:02x}".format(x) for x in ip_header)
    print("IP Header:", ip_header_str)

    # Decode TCP header
    tcp_header = packet_data[34:54]
    tcp_header_str = ":".join("{:02x}".format(x) for x in tcp_header)
    print("TCP Header:", tcp_header_str)

    # Decode payload (actual data)
    payload = packet_data[54:]
    print("Payload:", payload)

def sniff_packets(interface_name):
    print("[*] Sniffing packets on interface", interface_name)
    try:
        # Create a raw socket
        conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        # Bind the socket to the interface
        conn.bind((netifaces.ifaddresses(interface_name)[netifaces.AF_INET][0]['addr'], 0))
        # Set socket options
        conn.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        # Enable promiscuous mode
        conn.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        try:
            while True:
                # Receive packet
                raw_data, addr = conn.recvfrom(65536)
                decode_packet(raw_data)
        except KeyboardInterrupt:
            print("\n[*] Stopping packet sniffing...")
            # Disable promiscuous mode
            conn.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
            conn.close()
    except Exception as e:
        print("Error:", e)

def main():
    interfaces = list_interfaces()
    if not interfaces:
        print("[-] No network interfaces found.")
        return
    index = int(input("[+] Enter the number of the interface to sniff: ")) - 1
    if 0 <= index < len(interfaces):
        interface_name = interfaces[index]
        sniff_packets(interface_name)
    else:
        print("[-] Invalid interface number.")

if __name__ == "__main__":
    main()

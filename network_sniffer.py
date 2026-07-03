from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

def packet_callback(packet):
    print("=" * 60)

    # Check if packet has an IP layer
    if packet.haslayer(IP):
        ip = packet[IP]

        print(f"Source IP      : {ip.src}")
        print(f"Destination IP : {ip.dst}")

        # Identify Protocol
        if packet.haslayer(TCP):
            tcp = packet[TCP]
            print("Protocol       : TCP")
            print(f"Source Port    : {tcp.sport}")
            print(f"Destination Port: {tcp.dport}")

        elif packet.haslayer(UDP):
            udp = packet[UDP]
            print("Protocol       : UDP")
            print(f"Source Port    : {udp.sport}")
            print(f"Destination Port: {udp.dport}")

        elif packet.haslayer(ICMP):
            print("Protocol       : ICMP")

        else:
            print(f"Protocol Number: {ip.proto}")

        # Display Payload (if present)
        if packet.haslayer(Raw):
            payload = packet[Raw].load

            try:
                print("Payload:")
                print(payload.decode(errors="ignore"))
            except:
                print(payload)

    print("=" * 60)


print("Starting Packet Sniffer...")
print("Press Ctrl+C to stop.\n")

sniff(prn=packet_callback, store=False)

from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime


def analyze_packet(packet):
    """Analyze and display captured network packets."""

    if IP not in packet:
        return

    ip = packet[IP]

    # Identify protocol and ports
    if TCP in packet:
        protocol = "TCP"
        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport

    elif UDP in packet:
        protocol = "UDP"
        source_port = packet[UDP].sport
        destination_port = packet[UDP].dport

    elif ICMP in packet:
        protocol = "ICMP"
        source_port = "-"
        destination_port = "-"

    else:
        protocol = f"IP Protocol {ip.proto}"
        source_port = "-"
        destination_port = "-"

    print("\n" + "=" * 60)
    print("Time:             ", datetime.now().strftime("%H:%M:%S"))
    print("Protocol:         ", protocol)
    print("Source IP:        ", ip.src)
    print("Destination IP:   ", ip.dst)
    print("Source Port:      ", source_port)
    print("Destination Port: ", destination_port)
    print("Packet Size:      ", len(packet), "bytes")

    # Display a limited payload preview
    if Raw in packet:
        payload = bytes(packet[Raw].load)

        print("Payload Size:     ", len(payload), "bytes")
        print("Payload (Hex):    ", payload[:32].hex(" "))

        readable = "".join(
            chr(byte) if 32 <= byte <= 126 else "."
            for byte in payload[:64]
        )
        print("Payload Preview:  ", readable)
    else:
        print("Payload:           No Raw payload layer")

    print("=" * 60)


def start_sniffer():
    print("=" * 60)
    print("          BASIC NETWORK SNIFFER")
    print("=" * 60)
    print("Status: Capturing IPv4 packets")
    print("Press CTRL+C to stop.\n")

    try:
        sniff(
            filter="ip",
            prn=analyze_packet,
            store=False,
            promisc=False
        )

    except KeyboardInterrupt:
        print("\nSniffer stopped successfully.")

    except Exception as error:
        print("\nError:", error)
        print("Check Npcap installation and permissions.")


if __name__ == "__main__":
    start_sniffer()

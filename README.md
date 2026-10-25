# network-sniffer
# 🛡️Network Sniffer in Python

A beginner-friendly cybersecurity project that captures and analyzes live IPv4 network traffic using Python and Scapy. The tool displays packet information, including source and destination IP addresses, protocols, port numbers, packet size, and available payload data.

## ✨ Features

- 📡 **Live Packet Capture** — Capture IPv4 packets in real time.
- 🌐 **IP Address Analysis** — Display source and destination IP addresses.
- 🔍 **Protocol Detection** — Identify TCP, UDP, ICMP, and other IPv4 protocols.
- 🔌 **Port Information** — Extract source and destination ports for TCP and UDP packets.
- 📦 **Packet Size** — Display the size of captured packets in bytes.
- 📝 **Payload Inspection** — Show a hexadecimal representation and readable-text preview when a Raw payload layer is available.
- 🕒 **Timestamps** — Display the time each packet is processed.
- ⏹️ **Graceful Shutdown** — Stop packet capture using `Ctrl + C`.

## 🛠️ Technologies Used

- Python 3
- Scapy
- Npcap (Windows packet capture)
- Visual Studio Code

## 📂 Project Structure

```text
network-sniffer/
├── sniffer.py
└── README.md
```

## ⚙️ Installation

### Prerequisites

- Python 3 installed on your computer.
- Scapy installed.
- Npcap installed on Windows.
- Appropriate permissions to capture network traffic.

### 1. Clone the Repository

```bash
git clone https://github.com/zainab23-dev/network-sniffer.git
cd network-sniffer
```

### 2. Install Scapy

```bash
python -m pip install scapy
```

### 3. Install Npcap on Windows

Download Npcap from the official website:

https://npcap.com/#download

Npcap provides the packet-capture driver required for live capture with Scapy on Windows.

## ▶️ Usage

### 1. Run the Program

Open the project folder in VS Code and run:

```bash
python sniffer.py
```

If necessary, run the terminal with administrator privileges.

### 2. Generate Network Traffic

Open a second terminal and run:

```powershell
ping 8.8.8.8
```

### 3. Analyze the Output

The sniffer displays information about packets it captures, including:

- Timestamp
- Protocol
- Source IP address
- Destination IP address
- Source and destination ports
- Packet size
- Available payload size and preview

Press `Ctrl + C` to stop the program.

## 💻 Example Output

```text
============================================================
          BASIC NETWORK SNIFFER
============================================================
Status: Capturing IPv4 packets
Press CTRL+C to stop.

============================================================
Time:              18:35:12
Protocol:           ICMP
Source IP:          192.168.1.10
Destination IP:     8.8.8.8
Source Port:        -
Destination Port:   -
Packet Size:        84 bytes
Payload:            No Raw payload layer
============================================================
```

*Note: The output above is illustrative. Actual packet details depend on your network, capture interface, and traffic.*

## 🧠 How It Works

1. **Capture:** Scapy's `sniff()` function captures IPv4 packets.
2. **Analyze:** The program checks for an IP layer and extracts packet details.
3. **Identify:** TCP, UDP, and ICMP packets are identified.
4. **Extract:** Source and destination ports are displayed for TCP and UDP packets.
5. **Inspect:** The program displays packet size and a limited payload preview when available.
6. **Display:** Packet information is printed in the terminal with a timestamp.

## 🎯 Learning Objectives

This project demonstrates practical understanding of:

- Network traffic and packet capture.
- IPv4 packet structure.
- TCP, UDP, and ICMP protocols.
- IP addresses and port numbers.
- Payload inspection.
- Python functions, conditional statements, and exception handling.
- Basic network troubleshooting and traffic analysis.

## 🚀 Future Improvements

- Network interface selection.
- Protocol-based packet filtering.
- Packet counters and traffic statistics.
- Export packet summaries to CSV.
- Save captured packets in PCAP format.
- Add a graphical user interface.
- Visualize network traffic in real time.

## 🔐 Ethical Use

This project is intended for educational purposes and authorized network monitoring.

Only capture traffic on devices and networks you own or have explicit permission to monitor. Payloads can contain sensitive information. HTTPS traffic is generally encrypted, so captured packets do not automatically reveal readable application content.

## 👩‍💻 Author

**Zainab Asif**

GitHub: [@zainab23-dev](https://github.com/zainab23-dev)

Project: [Network Sniffer](https://github.com/zainab23-dev/network-sniffer)

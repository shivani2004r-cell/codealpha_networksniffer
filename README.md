# Basic Network Packet Sniffer using Python

## Overview

This project is a **Basic Network Packet Sniffer** developed in Python using the **Scapy** library. The application captures live network packets from the selected network interface and displays useful information such as source and destination IP addresses, protocol type, port numbers, and packet payload (when available).

This project is intended for educational purposes to understand how network packets are transmitted and analyzed in real time. It demonstrates the fundamentals of packet sniffing and network traffic analysis.

## Features

* Captures live network packets.
* Displays source and destination IP addresses.
* Identifies network protocols:

  * TCP
  * UDP
  * ICMP
* Displays source and destination port numbers.
* Prints packet payload data when available.
* Runs continuously until interrupted by the user (Ctrl + C).

## Technologies Used

* Python 3
* Scapy
* Npcap (Windows)

## Project Structure

```
network-sniffer/
│
├── network_sniffer.py
└── README.md
```

## Requirements

* Python 3.x
* Scapy library
* Npcap (required for Windows users)

Install Scapy:

```bash
pip install scapy
```

For Windows, install Npcap before running the program.

## How to Run

1. Install Python.
2. Install Scapy using pip.
3. Install Npcap (Windows only).
4. Open Command Prompt or PowerShell as Administrator.
5. Navigate to the project folder.
6. Run the program:

```bash
python network_sniffer.py
```

The program will begin capturing packets immediately.

## Sample Output

```
============================================================
Source IP       : 192.168.1.10
Destination IP  : 142.250.183.206
Protocol        : TCP
Source Port     : 51234
Destination Port: 443

Payload:
GET / HTTP/1.1
...
============================================================
```

## Learning Outcomes

By completing this project, you will learn:

* Basics of computer networking.
* Packet sniffing concepts.
* IP, TCP, UDP, and ICMP protocols.
* Network traffic analysis.
* Using the Scapy library for packet manipulation.
* Working with real-time packet capture in Python.

## Limitations

* Captures packets only from the active network interface.
* Encrypted traffic (HTTPS, SSH, etc.) cannot be read in plain text.
* Administrator privileges may be required.
* Intended for educational and ethical use only.

## Future Improvements

* Save captured packets to a PCAP file.
* Export packet data to CSV.
* Add filtering by IP address or protocol.
* Develop a graphical user interface (GUI).
* Display packet statistics and traffic visualization.

## Disclaimer

This project is created solely for educational and learning purposes. Use it only on networks you own or have explicit permission to monitor. Unauthorized packet sniffing may violate privacy policies and applicable laws.

## Author

**Shivani Rajora**
# codealpha_networksniffer

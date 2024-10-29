# Network Scanner

## Description

This project involves creating a simple network scanner using Python. The scanner can identify devices on a network and their open ports.

## Objectives

- Scan a network for active devices.
- Identify open ports on each device.

## Tools Used

- Python
- Scapy library

## Methodology

1. Use Scapy to send ARP requests and identify active devices.
2. Use socket programming to scan for open ports on each active device.

## Results

The script successfully identified active devices and their open ports on a local network.

## How to Run

1. Ensure you have Python and Scapy installed.
2. Run the script:

```bash
python network_scanner.py

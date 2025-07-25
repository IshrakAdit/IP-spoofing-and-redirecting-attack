from scapy.all import IP, ICMP, send
import sys
import time

src_ip = sys.argv[1]
dst_ip = sys.argv[2]
payload = sys.argv[3]
interval = float(sys.argv[4]) if len(sys.argv) > 4 else 3.0
count = int(sys.argv[5]) if len(sys.argv) > 5 else 10

print(f"[*] Sending {count} spoofed ICMP packets from {src_ip} to {dst_ip} every {interval} seconds...")

for i in range(1, count + 1):
    pkt = IP(src=src_ip, dst=dst_ip) / ICMP(type=8) / payload
    send(pkt, verbose=0)
    print(f"[>] Sent packet {i} to {dst_ip}")
    time.sleep(interval)

print("[*] Done sending packets.")

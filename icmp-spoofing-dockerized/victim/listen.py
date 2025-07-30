from scapy.all import sniff, IP, ICMP

def handle_reply(pkt):
    if pkt.haslayer(ICMP) and pkt[ICMP].type == 0:
        print(f"[Victim] Received ICMP Echo Reply from {pkt[IP].src} to {pkt[IP].dst}")

print("[Victim] Listening for ICMP replies...")
sniff(filter="icmp", prn=handle_reply, store=False)

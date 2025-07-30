from scapy.all import sniff, IP, ICMP

def detect_reply(pkt):
    if pkt.haslayer(ICMP) and pkt[ICMP].type == 0:  # Echo reply
        print(f"[!] Got ICMP Echo Reply from {pkt[IP].src} to {pkt[IP].dst}")

print("[*] Sniffing for replies to spoofed packet...")
sniff(filter="icmp", prn=detect_reply, store=False)

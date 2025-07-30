from scapy.all import sniff, IP, ICMP, send, Raw

packet_count = 0  

def auto_reply(pkt):
    global packet_count
    if pkt.haslayer(ICMP) and pkt[ICMP].type == 8:
        packet_count += 1
        print(f"[{packet_count}] Got packet: {pkt.summary()}")
        
        ip = IP(src=pkt[IP].dst, dst=pkt[IP].src)
        icmp = ICMP(type=0, id=pkt[ICMP].id, seq=pkt[ICMP].seq)
        payload = ("Reply to: " + pkt[Raw].load.decode(errors='ignore')) if pkt.haslayer(Raw) else ""
        reply = ip / icmp / payload
        send(reply, verbose=0)
        print(f"[+] Replied to spoofed ping from {pkt[IP].src}")

print("[*] Listening for ICMP Echo Requests on eth0...")
sniff(filter="icmp", prn=auto_reply, store=False, iface="eth0")
